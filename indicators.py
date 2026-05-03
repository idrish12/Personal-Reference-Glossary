import pandas as pd

import numpy as np

# Technical Indicators and Market Structure Module

def calculate_ema(data, period=14):

"""Calculates the Exponential Moving Average"""

    return data['close'].ewm(span=period, adjust=False).mean()

def calculate_rsi(data, period=14):

    """Calculates the Relative Strength Index"""
