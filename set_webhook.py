import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = os.getenv("PUBLIC_URL")

set_webhook_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
r = requests.post(set_webhook_url, json={"url": URL})
print(r.json())
