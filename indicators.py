import pandas as pd

import numpy as np

# Technical Indicators and Market Structure Module

def calculate_ema(data, period=14):

"""Calculates the Exponential Moving Average"""

    return data['close'].ewm(span=period, adjust=False).mean()

def calculate_rsi(data, period=14):

    """Calculates the Relative Strength Index"""

delta = data['close'].diff()

    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()

loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss

    return 100 - (100 / (1 + rs))
