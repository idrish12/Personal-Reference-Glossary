import pandas as pd

import numpy as np

from datetime import datetime, timedelta

# Historical Backtesting Engine for SMC Strategy

class Backtester:

def __init__(self, initial_capital=10000.0):

self.capital = initial_capital

self.trades = []

self.win_rate = 0.0

self.total_profit = 0.0
