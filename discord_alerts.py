import requests

import json

# Webhook Integration for Real-Time Trade Signals

WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_id_here"

def send_discord_alert(setup_type, asset, entry_price):

"""Pushes real-time FVG and OB tap alerts to a private server"""

message = f"🚨 SMC ALERT 🚨\\nAsset: {asset}\\nSetup: {setup_type}\\nPrice: ${entry_price}"

    payload = {

"username": "SMC Bot",

"content": message

    }       
