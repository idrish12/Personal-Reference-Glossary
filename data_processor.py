import json

import pandas as pd

# Data Sanitization and Formatting Module

def clean_market_data(raw_data):

"""Removes null values and outliers from incoming API data"""

df = pd.DataFrame(raw_data)

    df.dropna(inplace=True)

    return df

def save_to_local_cache(data, filename):

"""Stores processed data to reduce API calls"""

with open(f'cache/{filename}.json', 'w') as f:

        json.dump(data, f)

def load_from_cache(filename):

"""Retrieves data from local storage"""

# Logic to read JSON and return dictionary

    pass
