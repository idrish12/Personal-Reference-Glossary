import time

from risk_manager import RiskManager

# Simulating execution on historical order block tap

class StrategyTester:

def __init__(self, trading_pair="BTC/USDT"):

self.pair = trading_pair

        self.is_running = False

self.risk_module = RiskManager(1000)

    def load_historical_data(self):
