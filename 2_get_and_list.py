import os
from pathlib import Path
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

load_dotenv(override=True, dotenv_path=Path(__file__).resolve().parent / ".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)

def get_rich_menu_list():
    try:
        response = messaging_api.get_rich_menu_list()
        print(f"Total rich menus: {len(response.richmenus)}")
        for rm in response.richmenus:
            print(f"- {rm.rich_menu_id}: {rm.name}")
        return response
    except Exception as e:
        print(f"Error: {e}")

def get_rich_menu(rich_menu_id: str):
    try:
        response = messaging_api.get_rich_menu(rich_menu_id)
        print(f"Rich menu ID: {response.rich_menu_id}")
        print(f"Name: {response.name}")
        print(f"Chat Bar Text: {response.chat_bar_text}")
        print(f"Size: {response.size.width}x{response.size.height}")
        print(f"Areas: {len(response.areas)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_rich_menu_list()
    get_rich_menu("richmenu-ccdb12652964190503e5933af502dac5")
