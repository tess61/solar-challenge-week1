import pandas as pd
import os

def load_data(country):
    """Load the cleaned CSV for a given country."""
    filepath = f"../data/{country}_clean.csv"
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, parse_dates=['Timestamp'])
        return df
    else:
        return None

def get_available_countries():
    """Return a list of supported country codes (based on available CSVs)."""
    return ['benin', 'togo', 'sierraleone']
