import os
from pathlib import Path
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from pprint import pprint

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
        pprint(response)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    get_rich_menu_list()
