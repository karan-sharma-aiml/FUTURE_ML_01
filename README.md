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

📁 FUTURE_ML_01/
├─ 📁 data/
│  └─ 📄 sample_sales.csv
├─ 📁 notebook/
│  ├─ 📄 eda.ipynb
│  └─ 📄 model_experiments.ipynb
├─ 📁 screenshots/
│  ├─ 📁 1.Dashboard section/
│  │  ├─ 📄 01_dashboard_overview.png
│  │  ├─ 📄 02_sidebar_controls.png
│  │  └─ 📄 03_data_preview.png
│  ├─ 📁 2.Forecasting Section/
│  │  ├─ 📄 04_prophet_forecast.png
│  │  ├─ 📄 05_prophet_components_main.png
│  │  ├─ 📄 05_prophet_yearly.png
│  │  ├─ 📄 06_lstm_forecast.png
│  │  └─ 📄 07_combined_prophet_lstm.png
│  └─ 📁 3.Evaluation & Explainability/
│     ├─ 📄 08_rolling_bracket_table.png
│     ├─ 📄 09_Sharp_bar_chart.png
│     └─ 📄 10_feature_importance.png
├─ 📁 src/
│  ├─ 📁 __pycache__/                 
│  │  └─ 📄 *.cpython-312.pyc
│  ├─ 📄 backtesting.py
│  ├─ 📄 data_processing.py
│  ├─ 📄 lstm_model.py
│  ├─ 📄 prophet_model.py
│  ├─ 📄 utils.py
│  └─ 📄 xgb_baseline.py
├─ 📁 venv/                          
│  └─ 📄 pyvenv.cfg
├─ 📄 .gitignore
├─ 📄 LICENSE
├─ 📄 README.md
├─ 📄 requirements.txt
└─ 📄 streamlit_sales_forecast.py


✅ Features:

Straight, vertical structure

Folder = 📁, File = 📄

Easy to paste in README.md

Agar chaho to main README.md ke liye ek aur enhanced version bhi bana doon jisme project overview aur folder explanation bhi ho, jisse repo aur professional lage.

Chahoge ki main wo version bana doon?

You said:
bhai thoda attractive emoji dal
ChatGPT said:

Bhai, samajh gaya 😎 Main folder structure ko aur attractive aur expressive emojis ke saath bana deta hoon, jisse README.md kholte hi eye-catching lage.

🚀 **FUTURE_ML_01/**
├─ 📊 **data/**
│  └─ 🗂️ sample_sales.csv
├─ 📓 **notebook/**
│  ├─ 🔍 eda.ipynb
│  └─ 🤖 model_experiments.ipynb
├─ 📸 **screenshots/**
│  ├─ 🖥️ **1.Dashboard section/**
│  │  ├─ 📈 01_dashboard_overview.png
│  │  ├─ 🧩 02_sidebar_controls.png
│  │  └─ 🗃️ 03_data_preview.png
│  ├─ 📊 **2.Forecasting Section/**
│  │  ├─ 🔮 04_prophet_forecast.png
│  │  ├─ 📅 05_prophet_components_main.png
│  │  ├─ 📆 05_prophet_yearly.png
│  │  ├─ 🤖 06_lstm_forecast.png
│  │  └─ ⚡ 07_combined_prophet_lstm.png
│  └─ 🧠 **3.Evaluation & Explainability/**
│     ├─ 📋 08_rolling_bracket_table.png
│     ├─ 📊 09_Sharp_bar_chart.png
│     └─ 🌟 10_feature_importance.png
├─ 💻 **src/**
│  ├─ 🗂️ __pycache__/                 
│  │  └─ 📝 *.cpython-312.pyc
│  ├─ 📜 backtesting.py
│  ├─ 🛠️ data_processing.py
│  ├─ 🧠 lstm_model.py
│  ├─ 🔮 prophet_model.py
│  ├─ ⚙️ utils.py
│  └─ 🚀 xgb_baseline.py
├─ 🐍 **venv/**                          
│  └─ 📝 pyvenv.cfg
├─ 📝 .gitignore
├─ 📜 LICENSE
├─ 📖 README.md
├─ 📦 requirements.txt
└─ 🌐 streamlit_sales_forecast.py


✅ Features:

Folder aur files ke liye fun, meaningful emojis

Professional + attractive look

Directly README.md me paste kar sakte ho

Agar chaho to main ek aur version bana doon jisme har folder ke purpose ka short description bhi ho, jisse repo kholte hi samajh aa jaye kaunsa folder kya karta hai.

Chahiye kya wo version?

You said:
## 📂 Project Structure

📂 FUTURE_ML_01/
├─ 📂 data/
│  └─ 📄 sample_sales.csv
│
├─ 📂 notebook/
│  ├─ 📓 eda.ipynb
│  └─ 📓 model_experiments.ipynb
│
├─ 📂 screenshots/
│  ├─ 📂 1.Dashboard Section/
│  │  ├─ 🖼️ 01_dashboard_overview.png
│  │  ├─ 🖼️ 02_sidebar_controls.png
│  │
│  ├─ 📂 2.Forecasting Section/
│  │  ├─ 🖼️ 04_prophet_forecast.png
│  │  ├─ 🖼️ 05_prophet_components_main.png
│  │  ├─ 🖼️ 05_prophet_yearly.png
│  │  ├─ 🖼️ 06_lstm_forecast.png
│  │  └─ 🖼️ 07_combined_prophet_lstm.png
│  │
│  └─ 📂 3.Evaluation & Explainability/
│     ├─ 🖼️ 08_rolling_bracket_table.png
│     ├─ 🖼️ 09_Sharp_bar_chart.png
│     └─ 🖼️ 10_feature_importance.png
│
├─ 📂 src/
│  ├─ 📂 __pycache__/                 # compiled files (ignored in .gitignore)
│  py│  └─ *.cpython-312.pyc
│  ├─ ⚙️ backtesting.py
│  ├─ ⚙️ data_processing.py
│  ├─ ⚙️ lstm_model.py
│  ├─ ⚙️ prophet_model.py
│  ├─ ⚙️ utils.py
│  └─ ⚙️ xgb_baseline.
│
├─ 📂 venv/                           # DO NOT push to GitHub
│  └─ pyvenv.cfg, Scripts/, Lib/
│
├─ ⚙️ .gitignore
├─ 📜 LICENSE
├─ 📘 README.md
├─ 📦 requirements.txt ye structure h puarne wale se ye thoda missing h thik kar
ChatGPT said:

Bhai, samajh gaya 😎 Main tumhara complete folder structure ko missing parts ke saath, attractive emojis aur clean formatting me README.md-ready bana deta hoon. Yeh raha final version:

## 📂 Project Structure

📂 FUTURE_ML_01/
├─ 📂 data/
│  └─ 📄 sample_sales.csv
│
├─ 📂 notebook/
│  ├─ 📓 eda.ipynb
│  └─ 📓 model_experiments.ipynb
│
├─ 📂 screenshots/
│  ├─ 📂 1.Dashboard Section/
│  │  ├─ 🖼️ 01_dashboard_overview.png
│  │  ├─ 🖼️ 02_sidebar_controls.png
│  │  └─ 🖼️ 03_data_preview.png
│  │
│  ├─ 📂 2.Forecasting Section/
│  │  ├─ 🔮 04_prophet_forecast.png
│  │  ├─ 📅 05_prophet_components_main.png
│  │  ├─ 📆 05_prophet_yearly.png
│  │  ├─ 🤖 06_lstm_forecast.png
│  │  └─ ⚡ 07_combined_prophet_lstm.png
│  │
│  └─ 📂 3.Evaluation & Explainability/
│     ├─ 📋 08_rolling_bracket_table.png
│     ├─ 📊 09_Sharp_bar_chart.png
│     └─ 🌟 10_feature_importance.png
│
├─ 📂 src/
│  ├─ 📂 __pycache__/                 # compiled files (ignored in .gitignore)
│  │  └─ 📝 *.cpython-312.pyc
│  ├─ ⚙️ backtesting.py
│  ├─ ⚙️ data_processing.py
│  ├─ ⚙️ lstm_model.py
│  ├─ ⚙️ prophet_model.py
│  ├─ ⚙️ utils.py
│  └─ ⚙️ xgb_baseline.py
│
├─ 📂 venv/                           # DO NOT push to GitHub
│  └─ pyvenv.cfg, Scripts/, Lib/
│
├─ ⚙️ .gitignore
├─ 📜 LICENSE
├─ 📘 README.md
├─ 📦 requirements.txt
└─ 🌐 streamlit_sales_forecast.py


✅ Features:

Missing files added (03_data_preview.png, streamlit_sales_forecast.py)

Consistent emojis for folders 📂, files 📄, scripts ⚙️, images 🖼️

Clean and straight structure, ready for README.md

Agar chaho to main iske upar thoda aur professional touch bhi de sakta hoon jaise: folder ke purpose ka ek line description + emoji, jisse README aur impressive lage.

Chahiye main wo version bana doon?

You said:
## 📂 Project Structure

📂 FUTURE_ML_01/
├─ 📂 data/
│  └─ 📄 sample_sales.csv
│
├─ 📂 notebook/
│  ├─ 📓 eda.ipynb
│  └─ 📓 model_experiments.ipynb
│
├─ 📂 screenshots/
│  ├─ 📂 1.Dashboard Section/
│  │  ├─ 🖼️ 01_dashboard_overview.png
│  │  ├─ 🖼️ 02_sidebar_controls.png
│  │  └─ 🖼️ 03_data_preview.png
│  │
│  ├─ 📂 2.Forecasting Section/
│  │  ├─ 🔮 04_prophet_forecast.png
│  │  ├─ 📅 05_prophet_components_main.png
│  │  ├─ 📆 05_prophet_yearly.png
│  │  ├─ 🤖 06_lstm_forecast.png
│  │  └─ ⚡ 07_combined_prophet_lstm.png
│  │
│  └─ 📂 3.Evaluation & Explainability/
│     ├─ 📋 08_rolling_bracket_table.png
│     ├─ 📊 09_Sharp_bar_chart.png
│     └─ 🌟 10_feature_importance.png
│
├─ 📂 src/
│  ├─ 📂 __pycache__/                 # compiled files (ignored in .gitignore)
│  │  └─ 📝 *.cpython-312.pyc
│  ├─ ⚙️ backtesting.py
│  ├─ ⚙️ data_processing.py
│  ├─ ⚙️ lstm_model.py
│  ├─ ⚙️ prophet_model.py
│  ├─ ⚙️ utils.py
│  └─ ⚙️ xgb_baseline.py
│
├─ 📂 venv/                           # DO NOT push to GitHub
│  └─ pyvenv.cfg, Scripts/, Lib/
│
├─ ⚙️ .gitignore
├─ 📜 LICENSE
├─ 📘 README.md
├─ 📦 requirements.txt
└─ 🌐 streamlit_sales_forecast.py    mai jab isko readme.md me daal rha hu toh rows me ho ja rha h thik kar isko ki straight rahe  
ChatGPT said:

Ah, samajh gaya bhai 😎 Tum chahte ho README.md me ye folder structure straight line me ho, na ki har folder alag row me. Matlab ek compact, horizontal-style tree.

Yaha main tumhare liye straight, inline style bana raha hoon, jo README.md me properly straight dikhega:

## 📂 Project Structure

📂 FUTURE_ML_01/ → 📂 data/ → 📄 sample_sales.csv | 📂 notebook/ → 📓 eda.ipynb, 📓 model_experiments.ipynb | 📂 screenshots/ → 📂 1.Dashboard Section/ → 🖼️ 01_dashboard_overview.png, 🖼️ 02_sidebar_controls.png, 🖼️ 03_data_preview.png | 📂 2.Forecasting Section/ → 🔮 04_prophet_forecast.png, 📅 05_prophet_components_main.png, 📆 05_prophet_yearly.png, 🤖 06_lstm_forecast.png, ⚡ 07_combined_prophet_lstm.png | 📂 3.Evaluation & Explainability/ → 📋 08_rolling_bracket_table.png, 📊 09_Sharp_bar_chart.png, 🌟 10_feature_importance.png | 📂 src/ → 📂 __pycache__/ → 📝 *.cpython-312.pyc, ⚙️ backtesting.py, ⚙️ data_processing.py, ⚙️ lstm_model.py, ⚙️ prophet_model.py, ⚙️ utils.py, ⚙️ xgb_baseline.py | 📂 venv/ → pyvenv.cfg, Scripts/, Lib/ | ⚙️ .gitignore | 📜 LICENSE | 📘 README.md | 📦 requirements.txt | 🌐 streamlit_sales_forecast.py


✅ Features:

Straight horizontal line

Folder aur files ke liye emojis

Ready to paste in README.md

Agar chaho to main isko aur readable aur professional version bana doon jisme slightly line breaks with arrows use kar ke straight dikhe, par horizontal style maintain ho.

Chahiye kya main wo version bana doon?

You said:
## 📂 Project Structure

📂 FUTURE_ML_01/ → 📂 data/ → 📄 sample_sales.csv | 📂 notebook/ → 📓 eda.ipynb, 📓 model_experiments.ipynb | 📂 screenshots/ → 📂 1.Dashboard Section/ → 🖼️ 01_dashboard_overview.png, 🖼️ 02_sidebar_controls.png, 🖼️ 03_data_preview.png | 📂 2.Forecasting Section/ → 🔮 04_prophet_forecast.png, 📅 05_prophet_components_main.png, 📆 05_prophet_yearly.png, 🤖 06_lstm_forecast.png, ⚡ 07_combined_prophet_lstm.png | 📂 3.Evaluation & Explainability/ → 📋 08_rolling_bracket_table.png, 📊 09_Sharp_bar_chart.png, 🌟 10_feature_importance.png | 📂 src/ → 📂 __pycache__/ → 📝 *.cpython-312.pyc, ⚙️ backtesting.py, ⚙️ data_processing.py, ⚙️ lstm_model.py, ⚙️ prophet_model.py, ⚙️ utils.py, ⚙️ xgb_baseline.py | 📂 venv/ → pyvenv.cfg, Scripts/, Lib/ | ⚙️ .gitignore | 📜 LICENSE | 📘 README.md | 📦 requirements.txt | 🌐 streamlit_sales_forecast.py hmko aaise nhi chahiye straight chahiye 
ChatGPT said:

Ah, ab samajh gaya bhai 😎 Tum chahte ho README.md me ye pura folder structure vertically aligned straight tree style ho, jaise folder tree command me dikhta hai, rows me split ho, har level proper indentation ke saath, par horizontal na ho.

Yaha main bilkul straight aur professional version bana raha hoon, emojis ke saath:

## 📂 Project Structure

📂 FUTURE_ML_01/
├─ 📂 data/
│  └─ 📄 sample_sales.csv
├─ 📂 notebook/
│  ├─ 📓 eda.ipynb
│  └─ 📓 model_experiments.ipynb
├─ 📂 screenshots/
│  ├─ 📂 1.Dashboard Section/
│  │  ├─ 🖼️ 01_dashboard_overview.png
│  │  ├─ 🖼️ 02_sidebar_controls.png
│  │  └─ 🖼️ 03_data_preview.png
│  ├─ 📂 2.Forecasting Section/
│  │  ├─ 🔮 04_prophet_forecast.png
│  │  ├─ 📅 05_prophet_components_main.png
│  │  ├─ 📆 05_prophet_yearly.png
│  │  ├─ 🤖 06_lstm_forecast.png
│  │  └─ ⚡ 07_combined_prophet_lstm.png
│  └─ 📂 3.Evaluation & Explainability/
│     ├─ 📋 08_rolling_bracket_table.png
│     ├─ 📊 09_Sharp_bar_chart.png
│     └─ 🌟 10_feature_importance.png
├─ 📂 src/
│  ├─ 📂 __pycache__/                 # compiled files (ignored in .gitignore)
│  │  └─ 📝 *.cpython-312.pyc
│  ├─ ⚙️ backtesting.py
│  ├─ ⚙️ data_processing.py
│  ├─ ⚙️ lstm_model.py
│  ├─ ⚙️ prophet_model.py
│  ├─ ⚙️ utils.py
│  └─ ⚙️ xgb_baseline.py
├─ 📂 venv/                           # DO NOT push to GitHub
│  └─ pyvenv.cfg, Scripts/, Lib/
├─ ⚙️ .gitignore
├─ 📜 LICENSE
├─ 📘 README.md
├─ 📦 requirements.txt
└─ 🌐 streamlit_sales_forecast.py


✅ Features:

Vertical straight tree structure

Proper indentation har folder level ke liye

Emojis for folders 📂, scripts ⚙️, images 🖼️, notebooks 📓, etc.

Ready to paste in README.md

Agar chaho, main isko aur attractive bana sakta hoon jisme har folder ke liye 1-line description bhi ho, jisse README aur professional lage.

Chahiye mai wo version bana doon?

You said:
Bhai gir gaya ye jab readme.md me copy kr ke daal rha hu save Krnae ke baad ye chote ho ja rha(vertically)h gir jaha h vertical Krna h 
ChatGPT said:

Ah, ab samajh gaya bhai 😎 Tumhare problem ka reason ye hai: README.md me normal text ke through folder tree daalne par Markdown automatically wrap ya compress kar deta hai, isliye vertical alignment gir jaata hai.

Iska proper solution ye hai ki Markdown me code block use karo. Matlab ``` (triple backticks) ke andar daaloge, to GitHub README ya VS Code Markdown me exactly waise hi dikhega jaise tumne format kiya hai, aur vertical straight rahega.

Example:

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
│ ├─ 📂 pycache/ # compiled files (ignored in .gitignore)
│ │ └─ 📝 *.cpython-312.pyc
│ ├─ ⚙️ backtesting.py
│ ├─ ⚙️ data_processing.py
│ ├─ ⚙️ lstm_model.py
│ ├─ ⚙️ prophet_model.py
│ ├─ ⚙️ utils.py
│ └─ ⚙️ xgb_baseline.py
├─ 📂 venv/ # DO NOT push to GitHub
│ └─ pyvenv.cfg, Scripts/, Lib/
├─ ⚙️ .gitignore
├─ 📜 LICENSE
├─ 📘 README.md
├─ 📦 requirements.txt
└─ 🌐 streamlit_sales_forecast.py

✅ Notes:

Triple backticks (```) ke andar daalne se text fixed-width font me dikhega aur vertical tree structure girne nahi paayega.

GitHub README, VS Code, aur Markdown preview me exactly waise hi dikhega.

Tum chaaho to mai ye final version emojis ke saath ready-to-copy bana doon code block ke andar, jo bilkul professional dikhe.

Chahoge mai wo bana doon?

You said:
haa
ChatGPT said:

Perfect bhai 😎 Main tumhare liye final professional version bana raha hoon, README.md ke liye ready-to-copy, code block me, emojis ke saath, vertical straight tree structure:

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
│ ├─ 📂 pycache/ # compiled files (ignored in .gitignore)
│ │ └─ 📝 *.cpython-312.pyc
│ ├─ ⚙️ backtesting.py
│ ├─ ⚙️ data_processing.py
│ ├─ ⚙️ lstm_model.py
│ ├─ ⚙️ prophet_model.py
│ ├─ ⚙️ utils.py
│ └─ ⚙️ xgb_baseline.py
├─ 📂 venv/ # DO NOT push to GitHub
│ └─ pyvenv.cfg, Scripts/, Lib/
├─ ⚙️ .gitignore
├─ 📜 LICENSE
├─ 📘 README.md
├─ 📦 requirements.txt
└─ 🌐streamlit_sales_forecast.py
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

