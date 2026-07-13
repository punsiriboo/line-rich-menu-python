import os
from pathlib import Path
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

load_dotenv(override=True, dotenv_path=Path(__file__).resolve().parent / ".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)

def link_rich_menu_to_user(user_id: str, rich_menu_id: str):
    try:
        messaging_api.link_rich_menu_to_user(user_id, rich_menu_id)
        print(f"Linked rich menu {rich_menu_id} to user {user_id}")
    except Exception as e:
        print(f"Error: {e}")

def unlink_rich_menu_from_user(user_id: str):
    try:
        messaging_api.unlink_rich_menu_from_user(user_id)
        print(f"Unlinked rich menu from user {user_id}")
    except Exception as e:
        print(f"Error: {e}")
    
def get_user_rich_menu(user_id: str):
    try:
        response = messaging_api.get_rich_menu_id_of_user(user_id)
        print(f"User {user_id} rich menu ID: {response.rich_menu_id}")
        return response.rich_menu_id
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    user_id = "YOUR_USER_ID_HERE"
    rich_menu_id = "richmenu-b02b0a41d2d34534bf397100d2c9fefd"
    link_rich_menu_to_user(user_id, rich_menu_id)
