import requests

import json

# Webhook Integration for Real-Time Trade Signals

WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_id_here"

def send_discord_alert(setup_type, asset, entry_price):
