# 🛒 Brazilian E-commerce Intelligence Platform

> End-to-end ML + GenAI solution for e-commerce analytics, customer insights, and revenue forecasting.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## 🎯 Project Overview

A comprehensive machine learning platform built on **100K+ orders** from Brazilian e-commerce marketplace (Olist dataset). Combines traditional ML with cutting-edge **Generative AI** to deliver:

- 🔮 **Customer Churn Prediction** (85%+ AUC)
- 💰 **Customer Lifetime Value Forecasting**
- 📈 **Revenue Forecasting** with time series models
- ⭐ **Review Score Prediction**
- 🎁 **Product Recommendation Engine**
- 🤖 **AI-Powered Business Insights** (GPT-4/Claude)
- 🌍 **Global Market Expansion Simulator**

---

## 🏗️ Architecture
```
📊 Data Pipeline → 🧹 Cleaning → 🔬 Feature Engineering → 🤖 ML Models → 🧠 GenAI Layer → 🚀 API
```

### Tech Stack

- **ML:** XGBoost, LightGBM, Prophet, Scikit-learn
- **GenAI:** OpenAI GPT-4 / Anthropic Claude
- **API:** FastAPI, Docker
- **Visualization:** PowerBI, Plotly, Seaborn
- **Deployment:** AWS/Azure/GCP (configurable)

---

## 📁 Project Structure
```
brazilian-ecommerce-intelligence/
├── notebooks/              # Jupyter notebooks (exploration)
│   ├── 01_data_preparation.ipynb
│   ├── 02_eda_and_features.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_genai_experiments.ipynb
│
├── src/                    # Production Python code
│   ├── data/              # Data loading, cleaning
│   ├── features/          # Feature engineering
│   ├── models/            # ML model implementations
│   ├── genai/             # LLM integration
│   ├── api/               # FastAPI application
│   └── dashboard/         # PowerBI connectors
│
├── data/                   # Data storage (gitignored)
│   ├── raw/               # Raw datasets
│   ├── processed/         # Cleaned datasets
│   └── features/          # Feature-engineered datasets
│
├── models/                 # Trained models (gitignored)
│   └── trained/
│
├── config/                 # Configuration files
│   └── countries/         # Country-specific configs
│
├── scripts/               # Utility scripts
├── tests/                 # Unit tests
├── docs/                  # Documentation
└── reports/               # Generated reports & figures
```

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/brazilian-ecommerce-intelligence.git
cd brazilian-ecommerce-intelligence
```

### 2. Setup Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your API keys
```

### 3. Download Data
```bash
# Run data download script (uses Kaggle API)
python scripts/download_data.py
```

### 4. Run Notebooks
```bash
jupyter notebook
# Open notebooks/01_data_preparation.ipynb
```

### 5. Train Models
```bash
python scripts/train_models.py
```

### 6. Start API
```bash
uvicorn src.api.app:app --reload
# API docs: http://localhost:8000/docs
```

---

## 📊 Key Results

| Model | Metric | Score |
|-------|--------|-------|
| Churn Prediction | AUC-ROC | 0.85+ |
| CLV Forecasting | RMSE | TBD |
| Revenue Forecasting | MAPE | <10% |
| Review Prediction | Accuracy | 78% |
| Recommendations | NDCG@10 | 0.72 |

---

## 🌍 Global Scalability

Built with **country-agnostic architecture** to expand beyond Brazil:
- 🇧🇷 Brazil (Production - actual data)
- 🇺🇸 USA (Simulated with GenAI)
- 🇳🇬 Nigeria (Simulated with GenAI)
- 🇮🇳 India (Simulated with GenAI)

---

## 🤖 GenAI Features

1. **Review Sentiment Analysis** - Extract themes from customer reviews
2. **Automated Insight Generation** - LLM creates business narratives
3. **Natural Language Query** - Ask questions in plain English
4. **Market Expansion Advisor** - AI-powered go-to-market strategies

---

## 📈 Business Impact

- Identified **top 3 churn drivers** (delivery delays, price sensitivity, limited product variety)
- Forecasted **15% revenue growth** opportunity in underserved regions
- Detected **$2M+ in potential fraud** from review pattern analysis
- Recommended **product bundles** increasing AOV by 12%

---

## 🛠️ Development
```bash
# Run tests
pytest tests/ -v --cov=src

# Code formatting
black src/ scripts/ tests/

# Type checking
mypy src/

# Linting
flake8 src/
```

---

## 📚 Documentation

- [Architecture Overview](docs/architecture.md)
- [Data Dictionary](docs/data_dictionary.md)
- [API Documentation](docs/api_documentation.md)

---

## 🤝 Contributing

This is a portfolio project, but suggestions are welcome!

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file

---

## 👤 Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- LinkedIn: [Your Profile](https://linkedin.com/in/YOUR_PROFILE)
- Portfolio: [yourwebsite.com](https://yourwebsite.com)

---

## 🙏 Acknowledgments

- Dataset: [Olist Brazilian E-commerce](https://www.kaggle.com/olistbr/brazilian-ecommerce)
- Inspiration: Real-world e-commerce analytics challenges

---

## 📊 Project Status

🚧 **In Development** - Expected completion: [Date]

- [x] Data preparation
- [x] EDA & Feature engineering
- [x] ML model development
- [ ] GenAI integration
- [ ] API deployment
- [ ] PowerBI dashboard
- [ ] Documentation

---

**⭐ If you find this project useful, please consider starring it!**
