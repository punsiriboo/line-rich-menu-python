import os
from pathlib import Path
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models import RichMenuBulkLinkRequest, RichMenuBulkUnlinkRequest

load_dotenv(override=True, dotenv_path=Path(__file__).resolve().parent / ".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)


def link_rich_menu_to_users(user_ids: list, rich_menu_id: str):
    try:
        messaging_api.link_rich_menu_id_to_users(
            RichMenuBulkLinkRequest(rich_menu_id=rich_menu_id, user_ids=user_ids)
        )
        print(f"Linked rich menu {rich_menu_id} to {len(user_ids)} users")
    except Exception as e:
        print(f"Error: {e}")


def unlink_rich_menu_from_users(user_ids: list):
    try:
        messaging_api.unlink_rich_menu_id_from_users(
            RichMenuBulkUnlinkRequest(user_ids=user_ids)
        )
        print(f"Unlinked rich menu from {len(user_ids)} users")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    user_id = os.getenv("DESTINATION_USER_ID", "").strip().strip('"')
    user_ids = [user_id] if user_id else []
    rich_menu_id = "richmenu-ccdb12652964190503e5933af502dac5"
    link_rich_menu_to_users(user_ids, rich_menu_id)
    # unlink_rich_menu_from_users(user_ids)
