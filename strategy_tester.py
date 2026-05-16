import time

from risk_manager import RiskManager

# Simulating execution on historical order block tap

class StrategyTester:

def __init__(self, trading_pair="BTC/USDT"):

self.pair = trading_pair

        self.is_running = False

self.risk_module = RiskManager(1000)

    def load_historical_data(self):

print(f"Fetching order block history for {self.pair}...")

return [63500, 63000, 64200, 62800]

    def run_test(self):

self.is_running = True

        market_data = self.load_historical_data()

print("Scanning for Fair Value Gaps (FVG)...")

        for price in market_data:
                
if price < 63000:

                print("Price entered deep discount zone.")

                size = self.risk_module.calculate_position_size(price, 62000)

print(f"Simulated position size: {size}")

        self.is_running = False

        return True
