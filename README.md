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

## 📂 Project Structure - FUTURE_ML_01

📂 FUTURE_ML_01/ - Root project folder
├─ 📂 data/ - Contains dataset files
│  └─ 📄 sample_sales.csv - Sample sales dataset
├─ 📂 notebook/ - Jupyter notebooks for analysis
│  ├─ 📓 eda.ipynb - Exploratory Data Analysis
│  └─ 📓 model_experiments.ipynb - Model experimentation
├─ 📂 screenshots/ - Screenshots of dashboard and results
│  ├─ 📂 1.Dashboard Section/ - Dashboard UI images
│  │  ├─ 🖼️ 01_dashboard_overview.png - Overview of dashboard
│  │  ├─ 🖼️ 02_sidebar_controls.png - Sidebar controls screenshot
│  │  └─ 🖼️ 03_data_preview.png - Sample data preview
│  ├─ 📂 2.Forecasting Section/ - Forecasting model outputs
│  │  ├─ 🔮 04_prophet_forecast.png - Prophet forecast chart
│  │  ├─ 📅 05_prophet_components_main.png - Prophet main components
│  │  ├─ 📆 05_prophet_yearly.png - Yearly trend components
│  │  ├─ 🤖 06_lstm_forecast.png - LSTM forecast chart
│  │  └─ ⚡ 07_combined_prophet_lstm.png - Combined forecast
│  └─ 📂 3.Evaluation & Explainability/ - Evaluation visuals
│     ├─ 📋 08_rolling_bracket_table.png - Rolling bracket table
│     ├─ 📊 09_Sharp_bar_chart.png - Sharpe ratio chart
│     └─ 🌟 10_feature_importance.png - Feature importance chart
├─ 📂 src/ - Source code for models and utilities
│  ├─ 📂 __pycache__/ - Compiled Python files
│  │  └─ 📝 *.cpython-312.pyc
│  ├─ ⚙️ backtesting.py - Backtesting logic
│  ├─ ⚙️ data_processing.py - Data cleaning and preprocessing
│  ├─ ⚙️ lstm_model.py - LSTM model implementation
│  ├─ ⚙️ prophet_model.py - Prophet model implementation
│  ├─ ⚙️ utils.py - Utility functions
│  └─ ⚙️ xgb_baseline.py - XGBoost baseline model
├─ 📂 venv/ - Virtual environment (DO NOT push to GitHub)
│  └─ pyvenv.cfg, Scripts/, Lib/
├─ ⚙️ .gitignore - Git ignore file
├─ 📜 LICENSE - License file
├─ 📘 README.md - Project documentation
├─ 📦 requirements.txt - Python dependencies
└─ 🌐 streamlit_sales_forecast.py - Main Streamlit app


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

