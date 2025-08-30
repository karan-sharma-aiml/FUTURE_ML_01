# 🚀 AI-Powered Sales Forecasting Dashboard — Advanced

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![Prophet](https://img.shields.io/badge/Prophet-1.1+-green.svg)](https://facebook.github.io/prophet/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12+-orange.svg)](https://tensorflow.org)

> **Advanced Time Series Forecasting Dashboard with Multi-Model Ensemble, Uncertainty Quantification, and Explainable AI**

A production-ready forecasting system that combines **Prophet**, **LSTM Neural Networks**, and **XGBoost** with comprehensive model explainability using **SHAP**.

---

## 📊 Dashboard Preview

### 🏠 Main Dashboard  

![Dashboard Overview](./screenshots/1.Dashbard%20section/01_dashbard_overview.png)

Uploaded sales data preview in real time

---

### 🔮 Forecasting Models  
![Prophet Forecast](screenshots/2.Forecasting%20Section/04_prophet_forecast.png)  
*Prophet model prediction with seasonality components*  

![LSTM Forecast](screenshots/2.Forecasting%20Section/06_lstm_forecast.png)  
*LSTM Neural Network with MC Dropout based uncertainty*  

![Combined Models](screenshots/2.Forecasting%20Section/07_combined_prophet_lstm.png)  
*Comparison of Prophet & LSTM predictions*

---

### 📈 Model Evaluation & Explainability  
![Rolling Backtest](screenshots/3.Evaluation%20&%20Explainability/08_rolling_bracket_table.png)  
*Rolling-origin cross-validation metrics (MAE, RMSE, MAPE)*  

###  SHAP Bar Chart  
![SHAP Bar Chart](./screenshots/3.Evaluation%20%26%20Explainability/09_Sharp_bar_chart.png)

### Feature Importance
![Feature Importance](screenshots/3.Evaluation%20&%20Explainability/10_feature_importance.png)  
*XGBoost feature contributions visualized*

## 📂 Project Structure

📂 FUTURE_ML_01/
├─ 📂 data/
│ └─ 📄 sample_sales.csv
├─ 📂 notebook/
│ ├─ 📓 eda.ipynb
│ └─ 📓 model_experiments.ipynb
├─ 📂 screenshots/
│ ├─ 📂 1.Dashboard Section/
│ │ ├─ 🖼️ 01_dashboard_overview.png
│ │ ├─ 🖼️ 02_sidebar_controls.png
│ │ └─ 🖼️ 03_data_preview.png
│ ├─ 📂 2.Forecasting Section/
│ │ ├─ 🔮 04_prophet_forecast.png
│ │ ├─ 📅 05_prophet_components_main.png
│ │ ├─ 📆 05_prophet_yearly.png
│ │ ├─ 🤖 06_lstm_forecast.png
│ │ └─ ⚡ 07_combined_prophet_lstm.png
│ └─ 📂 3.Evaluation & Explainability/
│ ├─ 📋 08_rolling_bracket_table.png
│ ├─ 📊 09_Sharp_bar_chart.png
│ └─ 🌟 10_feature_importance.png
├─ 📂 src/
│ ├─ 📂 pycache/
│ │ └─ 📝 *.cpython-312.pyc
│ ├─ ⚙️ backtesting.py
│ ├─ ⚙️ data_processing.py
│ ├─ ⚙️ lstm_model.py
│ ├─ ⚙️ prophet_model.py
│ ├─ ⚙️ utils.py
│ └─ ⚙️ xgb_baseline.py
├─ 📂 venv/
│ └─ pyvenv.cfg, Scripts/, Lib/
├─ ⚙️ .gitignore
├─ 📜 LICENSE
├─ 📘 README.md
├─ 📦 requirements.txt
└─ 🌐 streamlit_sales_forecast.py


## 🌟 Key Features

### 🔬 **Advanced ML Models**
- **Facebook Prophet** with automatic seasonality detection and uncertainty intervals
- **LSTM Neural Networks** with Monte Carlo Dropout for uncertainty quantification  
- **XGBoost Baseline** with feature importance and SHAP explainability
- **Multi-model ensemble** with rolling-origin cross-validation

### 📊 **Professional Dashboard**
- **Interactive Streamlit interface** with real-time parameter tuning
- **Dynamic visualization** with Plotly charts
- **Comprehensive data preview** with automated feature engineering
- **Export functionality** for predictions and plots

### 🎯 **Production-Ready Architecture**
- **Modular codebase** with separation of concerns
- **Testing suite** with pytest
- **Config management** with YAML
- **Professional docs** & clean organization

---

## 🛠️ Technical Architecture

### **Pipeline**
```

Data Ingestion → Feature Engineering → Model Training →
Prediction Generation → Model Validation → Explainability Analysis

````

### **Tech Stack**
- **Backend**: Python 3.8+ (Pandas, NumPy, scikit-learn ecosystem)
- **ML Frameworks**: TensorFlow/Keras, Prophet, XGBoost
- **Explainability**: SHAP
- **Visualization**: Plotly
- **UI**: Streamlit

---

## 🚀 Quick Start

```bash
# Clone repo
git clone https://github.com/karan-sharma-aiml/FUTURE_ML_01.git
cd FUTURE_ML_01

# Setup env
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run streamlit_sales_forecast.py
````

---

## 📊 Model Performance (Example)

| Model   | MAE   | RMSE  | MAPE  | Coverage% | Training Time |
| ------- | ----- | ----- | ----- | --------- | ------------- |
| Prophet | 0.00  | 0.00  | 0.00% | 95.2%     | 2.3s          |
| LSTM    | 0.00  | 0.00  | 0.00% | 92.8%     | 45.7s         |
| XGBoost | 70.03 | 85.21 | 12.4% | -         | 1.8s          |

---

## 🎯 Business Applications

* **Retail Forecasting**: Inventory & demand planning
* **Revenue Forecasting**: Budget allocation
* **Resource Planning**: Workforce scheduling
* **Supply Chain Optimization**: Procurement & logistics

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit changes + add docs/tests
4. Submit PR 🎉

---

## 👨‍💻 Author

**Karan Sharma**
🎓 B.Tech CSE (AI/ML) Student @ CGC University, Mohali

💡 Focus: Time Series | Deep Learning | Explainable AI
📧 Email: [karan.sharma@email.com](mailto:karan.sharma@email.com)
🔗 [LinkedIn](https://www.linkedin.com/in/karan-sharma-167957271)
🐙 [GitHub](https://github.com/karan-sharma-aiml)

---

<div align="center">

⭐ **Star this repo if you find it useful!** ⭐

*Built with ❤️ for the AI/ML community*

</div>
```

---

