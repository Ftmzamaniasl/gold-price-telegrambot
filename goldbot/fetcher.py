import requests
from .config import GOLD_PRICE_URL

def fetch_gold_price(API_KEY):
    headers =headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    try:
        response = requests.get(GOLD_PRICE_URL, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        gold_18 = data["data"]["prices"]["GOLD18K"]["current"]
        gold_24 = data["data"]["prices"]["GOLD24K"]["current"]
        price = f"قیمت لحظه‌ای طلای ۱۸ عیار:,{gold_18} قیمت لحظه‌ای طلای 24 عیار:, {gold_24}"
        return price
    except Exception as e:
        return f"Error fecthing price : {e}"


