import time
import pandas as pd
import scipy.stats
import streamlit as st

# State Initialization
if "experiment_no" not in st.session_state:
    st.session_state["experiment_no"] = 0

if "df_experiments" not in st.session_state:
    st.session_state["df_experiments"] = pd.DataFrame(columns=["#_experimento", "Iteraciones", "Media"])

# UI Header
st.header("Simulación de lanzamientos de una moneda")

# Chart for animated mode
chart_mean = st.line_chart([0.5], height=300)

def toss_coin_animated(n: int):
    """Simula n lanzamientos con animación en tiempo real."""
    outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    cumulative_means = []
    count_heads = 0

    for i, result in enumerate(outcomes, start=1):
        count_heads += result
        mean_ = count_heads / i
        cumulative_means.append(mean_)
        chart_mean.add_rows([mean_])
        time.sleep(0.02)  # smooth animation

    return outcomes, cumulative_means, count_heads


def toss_coin_fast(n: int):
    """Simulación vectorizada, sin animación (mucho más rápida)."""
    outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    cumulative_means = outcomes.cumsum() / (pd.RangeIndex(len(outcomes)) + 1)
    count_heads = outcomes.sum()
    return outcomes, cumulative_means.tolist(), count_heads



# Controls
num_experiment_placeholder = st.empty()
num_trials = st.slider("¿Número de lanzamientos?", 1, 3000, 20)
fast_mode = st.checkbox("Modo rápido (sin animación)", value=False)
start_button = st.button("Ejecutar")
download_placeholder = st.empty()
running_placeholder = st.empty()

# Simulation Trigger
if start_button:
    st.session_state["experiment_no"] += 1
    running_placeholder.write(f"Ejecutando experimento #{st.session_state['experiment_no']}...")

    # choose mode
    if fast_mode:
        outcomes, means, heads = toss_coin_fast(num_trials)
    else:
        outcomes, means, heads = toss_coin_animated(num_trials)

    final_mean = means[-1]
    running_placeholder.empty()

    # Save experiment result
    st.session_state["df_experiments"] = pd.concat(
        [
            st.session_state["df_experiments"],
            pd.DataFrame([[st.session_state["experiment_no"], num_trials, final_mean]],
                         columns=["#_experimento", "Iteraciones", "Media"]),
        ],
        ignore_index=True,
    )

    # Save raw experiment data
    st.session_state["last_experiment_data"] = pd.DataFrame({
        "resultado": outcomes,
        "media_acumulada": means,
        "caras_acumuladas": pd.Series(outcomes).cumsum()
    })

    num_experiment_placeholder.write(f"Experimento #{st.session_state['experiment_no']} completado")
    # Download button
    with download_placeholder.container():
        st.subheader("Descargar Datos del Experimento")
        csv_exp = st.session_state["last_experiment_data"].to_csv(index=False)
        st.download_button(
            "Descargar CSV de resultados",
            csv_exp,
            file_name=f"experimento_{st.session_state['experiment_no']}.csv"
        )
    
    # Additional Plots / Results
    st.subheader("Resultados del Experimento")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total de 'caras' (1s)", heads)
        st.metric("Media final", round(final_mean, 4))

    with col2:
        st.metric("Valor esperado (p)", 0.5)
        st.metric("Error absoluto", abs(final_mean - 0.5))

    st.subheader("Distribución de Resultados")
    st.bar_chart(pd.Series(outcomes).value_counts().sort_index())

    st.subheader("Media Acumulada vs Valor Esperado")
    df_compare = pd.DataFrame({
        "media_acumulada": means,
        "valor_esperado": [0.5] * len(means),
    })
    st.line_chart(df_compare)


# Experiment History
st.subheader("Historial de Experimentos")
st.write(st.session_state["df_experiments"])

# History CSV Download
csv = st.session_state["df_experiments"].to_csv(index=False)
st.download_button("Descargar CSV", csv, "historial_experimentos.csv")

