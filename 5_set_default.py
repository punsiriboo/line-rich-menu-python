import os
from pathlib import Path
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

load_dotenv(override=True, dotenv_path=Path(__file__).resolve().parent / ".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)

def set_default_rich_menu(rich_menu_id: str):
    try:
        messaging_api.set_default_rich_menu(rich_menu_id)
        print(f"Set default rich menu: {rich_menu_id}")
    except Exception as e:
        print(f"Error: {e}")

def get_default_rich_menu():
    try:
        response = messaging_api.get_default_rich_menu()
        print(f"Default rich menu ID: {response.rich_menu_id}")
        return response.rich_menu_id
    except Exception as e:
        print(f"Error: {e}")
        return None

def cancel_default_rich_menu():
    try:
        messaging_api.cancel_default_rich_menu()
        print("Canceled default rich menu")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    set_default_rich_menu("richmenu-595db7774db65aa1484bb2a8d44273f6")
