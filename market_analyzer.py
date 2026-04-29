import time
import datetime
import random

# Initializing the market analysis tool
print("Starting Market Structure Analyzer...")

# Tracked assets for liquidity analysis
target_assets = {
    "BTC": {"current_price": 0, "order_block": 62000},
    "SUI": {"current_price": 0, "order_block": 1.45},
    "XMR": {"current_price": 0, "order_block": 130}
}

def fetch_simulated_price(ticker):
    """Simulates fetching real-time market data via API"""
    base_prices = {"BTC": 64000, "SUI": 1.50, "XMR": 135}
    volatility = random.uniform(-0.02, 0.02)
    return round(base_prices[ticker] * (1 + volatility), 2)

def update_market_data():
    """Updates the dictionary with fresh market prices"""
    for asset in target_assets:
        target_assets[asset]["current_price"] = fetch_simulated_price(asset)
        print(f"Updated {asset} price: ${target_assets[asset]['current_price']}")

def check_order_blocks():
    """Checks if current price is tapping into historical order blocks"""
    for asset, data in target_assets.items():
        if abs(data["current_price"] - data["order_block"]) < (data["current_price"] * 0.01):
            print(f"ALERT: {asset} is testing the order block at {data['order_block']}")
