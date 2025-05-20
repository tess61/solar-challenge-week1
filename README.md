# Solar Challenge Week 1

## Setup Instructions

### Clone the repo
```bash
    git clone https://github.com/your-username/solar-challenge-week1.git
    cd solar-challenge-week1
```

### Create virtual environment
```bash
    py -m venv venv
    source venv/Scripts/activate
```

### Install dependencies
```bash
    pip install -r requirements.txt
```

### Ensure cleaned CSVs are in the /data folder, named like:
```bash
    data/benin_clean.csv
    data/togo_clean.csv
    data/sierraleone_clean.csv
```

### Run the Streamlit app:
```bash
    streamlit run streamlit_app/app.py
```

## Folder Structure
```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/ # EDA and comparison Jupyter notebooks
│   ├── sierraleone_eda.ipynb
│   ├── benin_eda.ipynb
│   ├── compare_countries.ipynb
│   └── togo_eda.ipynb
├── streamlit_app/
│   ├── pages/
│   ├── utils/
│       └── data_loader.py # Helper function to load data
│   └── app.py Main Streamlit app
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
```