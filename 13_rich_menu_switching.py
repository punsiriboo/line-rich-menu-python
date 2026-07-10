import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models import (
    CreateRichMenuAliasRequest,
    RichMenuArea,
    RichMenuBounds,
    RichMenuRequest,
    RichMenuSize,
    RichMenuSwitchAction,
)

load_dotenv(override=True, dotenv_path="../.env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)

ALIAS_A = "richmenu-alias-a"
ALIAS_B = "richmenu-alias-b"

def build_switch_menu(name: str, chat_bar_text: str, switch_alias_id: str, switch_data: str, switch_side: str):
    switch_bounds = RichMenuBounds(x=1250, y=0, width=1250, height=843)
    if switch_side == "left":
        switch_bounds = RichMenuBounds(x=0, y=0, width=1250, height=843)

    return RichMenuRequest(
        size=RichMenuSize(width=2500, height=843),
        selected=True,
        name=name,
        chat_bar_text=chat_bar_text,
        areas=[
            RichMenuArea(
                bounds=switch_bounds,
                action=RichMenuSwitchAction(
                    type="richmenuswitch",
                    rich_menu_alias_id=switch_alias_id,
                    data=switch_data,
                ),
            )
        ],
    )

def setup_switching_menus():
    try:
        menu_a = build_switch_menu("Menu A", "Tab A", ALIAS_B, "switched-to-b", "right")
        menu_b = build_switch_menu("Menu B", "Tab B", ALIAS_A, "switched-to-a", "left")

        menu_a_id = messaging_api.create_rich_menu(menu_a).rich_menu_id
        menu_b_id = messaging_api.create_rich_menu(menu_b).rich_menu_id

        messaging_api.create_rich_menu_alias(
            CreateRichMenuAliasRequest(rich_menu_alias_id=ALIAS_A, rich_menu_id=menu_a_id)
        )
        messaging_api.create_rich_menu_alias(
            CreateRichMenuAliasRequest(rich_menu_alias_id=ALIAS_B, rich_menu_id=menu_b_id)
        )

        print(f"Created menu A: {menu_a_id}")
        print(f"Created menu B: {menu_b_id}")
        print("Next: upload images with 3_set_image.py, then link menu A to user")
        return menu_a_id, menu_b_id
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def link_start_menu_to_user(user_id: str, rich_menu_id: str):
    try:
        messaging_api.link_rich_menu_to_user(user_id, rich_menu_id)
        print(f"Linked start menu {rich_menu_id} to user {user_id}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    menu_a_id, _ = setup_switching_menus()
    if menu_a_id:
        link_start_menu_to_user("YOUR_USER_ID_HERE", menu_a_id)
