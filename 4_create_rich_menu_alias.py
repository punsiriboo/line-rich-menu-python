import os
from pathlib import Path
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models import CreateRichMenuAliasRequest

load_dotenv(override=True, dotenv_path=Path(__file__).resolve().parent / ".env")

configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)


def create_rich_menu_alias(rich_menu_alias_id: str, rich_menu_id: str):
    try:
        messaging_api.create_rich_menu_alias(
            CreateRichMenuAliasRequest(
                rich_menu_alias_id=rich_menu_alias_id,
                rich_menu_id=rich_menu_id,
            )
        )
        print(f"Created alias {rich_menu_alias_id} -> {rich_menu_id}")
    except Exception as e:
        print(f"Error: {e}")


def delete_rich_menu_alias(rich_menu_alias_id: str):
    try:
        messaging_api.delete_rich_menu_alias(rich_menu_alias_id)
        print(f"Deleted alias: {rich_menu_alias_id}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    create_rich_menu_alias("test-alias-105601", "richmenu-ccdb12652964190503e5933af502dac5")
    # delete_rich_menu_alias("test-alias-105601")
