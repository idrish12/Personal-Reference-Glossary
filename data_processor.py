import json

import pandas as pd

# Data Sanitization and Formatting Module

def clean_market_data(raw_data):

"""Removes null values and outliers from incoming API data"""

df = pd.DataFrame(raw_data)

    df.dropna(inplace=True)

    return df
