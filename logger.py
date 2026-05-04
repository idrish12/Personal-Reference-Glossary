import logging

import os

from datetime import datetime

# Trading Activity Logger Module

def setup_logger():

"""Configures the logging system for market alerts"""

    if not os.path.exists('logs'):

os.makedirs('logs')

    current_date = datetime.now().strftime("%Y-%m-%d")

log_filename = f"logs/trading_activity_{current_date}.log"

    logging.basicConfig(

        level=logging.INFO,
