import os
from datetime import datetime, timedelta
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv
from linebot.v3.insight import ApiClient, Configuration, Insight

load_dotenv(override=True, dotenv_path=Path(__file__).resolve().parent / ".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
insight_api = Insight(api_client)

def date_range(days: int = 7):
    to_date = datetime.now()
    from_date = to_date - timedelta(days=days)
    return from_date.strftime("%Y%m%d"), to_date.strftime("%Y%m%d")

def get_rich_menu_summary(rich_menu_id: str, from_date: str, to_date: str):
    try:
        response = insight_api.get_rich_menu_insight_summary(rich_menu_id, from_date, to_date)
        print(f"Summary {rich_menu_id} ({from_date} - {to_date})")
        pprint(response)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_rich_menu_daily(rich_menu_id: str, from_date: str, to_date: str):
    try:
        response = insight_api.get_rich_menu_insight_daily(rich_menu_id, from_date, to_date)
        print(f"Daily {rich_menu_id} ({from_date} - {to_date})")
        pprint(response)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    rich_menu_id = "richmenu-1d2e62eb1e49dc5e98de2a3a72ae4369"
    from_date, to_date = date_range(7)
    get_rich_menu_summary(rich_menu_id, from_date, to_date)
    get_rich_menu_daily(rich_menu_id, from_date, to_date)
