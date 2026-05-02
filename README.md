# Market Analyzer
# Smart Money Concepts (SMC) Market Analyzer

> An automated Python tool for identifying institutional trading levels.

## Overview

This script tracks major cryptocurrencies to detect high-probability setups.

It focuses on market structure shifts rather than retail indicators.

## Core Features

* **Order Block Detection:** Identifies the last bearish/bullish candles before major impulsive moves.

* **Fair Value Gaps (FVG):** Scans for pricing inefficiencies and imbalances.

* **Liquidity Sweeps:** Alerts when price targets resting stop-loss clusters.

* **Premium/Discount Zones:** Calculates the equilibrium of current price legs.

## Installation Requirements

You must have Python 3.10 or higher installed.

1. Clone this repository to your local machine.

2. Open your terminal or command prompt.

3. Navigate into the project folder.

4. Run the following command to install dependencies:

pip install -r requirements.txt

## Configuration

Before running the tool, you need to set up your preferences.

Open the config.json file in your code editor.

Adjust the macro_trend and execution timeframes to match your trading style.

## Usage

To start the scanner, run the main script from your terminal:

python market_analyzer.py

The terminal will output live data and print alerts when levels are tapped.

## Risk Warning

This tool is for educational purposes and market analysis only.

It does not execute live trades automatically.

Always use proper risk management and never risk more than 1-2% of your account.

## Future Updates

* Adding integration with Telegram for mobile push notifications.

* Adding Wyckoff accumulation phase detection.

* Expanding the watchlist to include traditional forex pairs.
