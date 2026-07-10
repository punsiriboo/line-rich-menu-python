import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

load_dotenv(override=True, dotenv_path="../.env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)

def create_rich_menu_alias(rich_menu_alias_id: str, rich_menu_id: str):
    try:
        messaging_api.create_rich_menu_alias(rich_menu_alias_id, rich_menu_id)
        print(f"Created alias {rich_menu_alias_id} -> {rich_menu_id}")
    except Exception as e:
        print(f"Error: {e}")

def get_rich_menu_alias(rich_menu_alias_id: str):
    try:
        response = messaging_api.get_rich_menu_alias(rich_menu_alias_id)
        print(f"Alias {rich_menu_alias_id} -> {response.rich_menu_id}")
        return response.rich_menu_id
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_rich_menu_alias_list():
    try:
        response = messaging_api.get_rich_menu_alias_list()
        print(f"Total aliases: {len(response.aliases)}")
        for alias in response.aliases:
            print(f"- {alias.rich_menu_alias_id} -> {alias.rich_menu_id}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

def update_rich_menu_alias(rich_menu_alias_id: str, rich_menu_id: str):
    try:
        messaging_api.update_rich_menu_alias(rich_menu_alias_id, rich_menu_id)
        print(f"Updated alias {rich_menu_alias_id} -> {rich_menu_id}")
    except Exception as e:
        print(f"Error: {e}")

def delete_rich_menu_alias(rich_menu_alias_id: str):
    try:
        messaging_api.delete_rich_menu_alias(rich_menu_alias_id)
        print(f"Deleted alias: {rich_menu_alias_id}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    alias_id = "my-alias"
    rich_menu_id = "richmenu-595db7774db65aa1484bb2a8d44273f6"
    create_rich_menu_alias(alias_id, rich_menu_id)
