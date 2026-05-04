import logging

import os

from datetime import datetime

# Trading Activity Logger Module

def setup_logger():

"""Configures the logging system for market alerts"""

    if not os.path.exists('logs'):
