# 🪙 Coin Flip Simulator

An interactive **Streamlit** web app that simulates coin flips and visualizes the results in real time.  
The user can set the number of flips, choose between **animated** or **fast vectorized** mode, run multiple experiments, and download both the **raw data** and the **experiment history**.  
The app shows how the empirical mean converges to the theoretical probability (0.5), provides summary metrics, and displays multiple visualizations including the running mean and the distribution of outcomes.


---

## 🚀 Live Demo  

Run the app instantly on Render:  
👉 **https://**

---

## 🧠 Overview

This app demonstrates how randomness behaves in the long run by simulating repeated coin tosses.  
It uses **Python**, **NumPy**, and **Matplotlib** to calculate and plot the frequency of outcomes, making it a fun and simple introduction to probability concepts.

---

## 📌 Features  

- 🪙 Simulate thousands of coin flips in milliseconds  
- 📊 Automatic probability visualization  
- 🔁 Interactive UI with immediate feedback  
- 📈 Clean bar chart comparing heads vs. tails  
- ⚡ Built with lightweight, easy-to-understand code  
- 🧮 Great introduction to randomness + Monte Carlo ideas  
- ⬇️ Download data points as CSV

---

## ⚡ Technologies Used

- **Python 3**  
- **Streamlit** — for the interactive web interface  
- **NumPy** — for random simulations  
- **Matplotlib / Plotly** — for visualization  
- **Pandas** — for data handling (optional but supported)

## 🛠️ Installation

Clone the repository:
    git clone https://github.com/armandaske/monedas-streamlit.git
    cd monedas-streamlit

Install dependencies:
    pip install -r requirements.txt

Run the app:
    streamlit run app.py  or  python -m streamlit run app.py
