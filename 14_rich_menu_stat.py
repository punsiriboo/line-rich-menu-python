import os
from datetime import datetime, timedelta
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv(override=True, dotenv_path="../.env")
access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
base_url = "https://api.line.me/v2/bot/insight/richmenu"

def date_range(days: int = 7):
    to_date = datetime.now()
    from_date = to_date - timedelta(days=days)
    return from_date.strftime("%Y%m%d"), to_date.strftime("%Y%m%d")

def _get(path: str, params: dict):
    response = requests.get(
        f"{base_url}/{path}",
        params=params,
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()

def get_rich_menu_summary(rich_menu_id: str, from_date: str, to_date: str):
    try:
        data = _get(f"{rich_menu_id}/summary", {"from": from_date, "to": to_date})
        print(f"Summary {rich_menu_id} ({from_date} - {to_date})")
        pprint(data)
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_rich_menu_daily(rich_menu_id: str, from_date: str, to_date: str):
    try:
        data = _get(f"{rich_menu_id}/daily", {"from": from_date, "to": to_date})
        print(f"Daily {rich_menu_id} ({from_date} - {to_date})")
        pprint(data)
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    rich_menu_id = "richmenu-595db7774db65aa1484bb2a8d44273f6"
    from_date, to_date = date_range(7)
    get_rich_menu_summary(rich_menu_id, from_date, to_date)
    get_rich_menu_daily(rich_menu_id, from_date, to_date)
