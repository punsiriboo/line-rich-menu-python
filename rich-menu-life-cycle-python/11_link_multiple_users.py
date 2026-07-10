import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

load_dotenv(override=True, dotenv_path="../.env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)

def link_rich_menu_to_users(user_ids: list, rich_menu_id: str):
    try:
        messaging_api.link_rich_menu_to_users(user_ids, rich_menu_id)
        print(f"Linked rich menu {rich_menu_id} to {len(user_ids)} users")
    except Exception as e:
        print(f"Error: {e}")

def unlink_rich_menu_from_users(user_ids: list):
    try:
        messaging_api.unlink_rich_menu_from_users(user_ids)
        print(f"Unlinked rich menu from {len(user_ids)} users")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    user_ids = ["USER_ID_1", "USER_ID_2", "USER_ID_3"]
    rich_menu_id = "richmenu-595db7774db65aa1484bb2a8d44273f6"
    link_rich_menu_to_users(user_ids, rich_menu_id)
