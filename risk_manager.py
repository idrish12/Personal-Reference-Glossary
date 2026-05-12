import math

from config import config_data

# Risk Management and Position Sizing Module

class RiskManager:

    def __init__(self, account_balance):

self.balance = account_balance

        self.max_risk_percent = 0.01  # Default 1% risk per trade

def calculate_position_size(self, entry_price, stop_loss):

"""Determines how much to buy based on risk parameters"""
