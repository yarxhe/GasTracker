# config.py

import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


PHOTO_PATH = os.getenv("PHOTO_PATH", "static/bot1.jpg") # "static/bot1.jpg" - значение по умолчанию
FOOTER_TEXT = os.getenv("FOOTER_TEXT", "\n\nProd by @devheadb")


SEND_INTERVAL_SECONDS = int(os.getenv("SEND_INTERVAL_SECONDS", 60))
CHECK_INTERVAL_SECONDS = int(os.getenv("CHECK_INTERVAL_SECONDS", 10))


GAS_THRESHOLDS = {
    "ok": int(os.getenv("GAS_THRESHOLD_OK", 15)),
    "warn": int(os.getenv("GAS_THRESHOLD_WARN", 25))
}


NETWORKS = {
    "ETH": {
        "url": os.getenv("RPC_URL_ETH"),
        "type": "evm"
    },
    "BLAST": {
        "url": os.getenv("RPC_URL_BLAST"),
        "type": "evm"
    },
    "SCROLL": {
        "url": os.getenv("RPC_URL_SCROLL"),
        "type": "evm"
    },
    "LINEA": {
        "url": os.getenv("RPC_URL_LINEA"),
        "type": "evm"
    },
    "BASE": {
        "url": os.getenv("RPC_URL_BASE"),
        "type": "evm"
    },
    "STARKNET": {
        "url": os.getenv("RPC_URL_STARKNET"),
        "type": "starknet"
    }
}


if not TELEGRAM_TOKEN or not CHAT_ID:
    raise ValueError("TELEGRAM_BOT_TOKEN и CHAT_ID должны быть установлены в .env файле")

for network_name, details in NETWORKS.items():
    if not details["url"]:
        raise ValueError(f"RPC URL для сети {network_name} не задан в .env файле (переменная RPC_URL_{network_name})")