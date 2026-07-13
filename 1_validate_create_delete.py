import os
from pathlib import Path
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, RichMenuRequest
from linebot.v3.messaging.models import CreateRichMenuAliasRequest

load_dotenv(override=True, dotenv_path=Path(__file__).resolve().parent / ".env")

configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration) 
messaging_api = MessagingApi(api_client)


def create_rich_menus(rich_menu_file: str):
    try:
        with open(rich_menu_file, "r") as f: richmenu_json = f.read()
        rich_menu_request = RichMenuRequest.from_json(richmenu_json)
        messaging_api.validate_rich_menu_object(rich_menu_request=rich_menu_request)
        api_response = messaging_api.create_rich_menu(rich_menu_request=rich_menu_request) 
        print(f"Successfully created rich menu from {rich_menu_file} with ID: {api_response.rich_menu_id}")
        return api_response.rich_menu_id
    except Exception as e:
        print(f"Error: {e}")
        return None

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

def delete_rich_menu(rich_menu_id: str):
    try:
        messaging_api.delete_rich_menu(rich_menu_id)
        print(f"Deleted rich menu: {rich_menu_id}")
    except Exception as e:
        print(f"Error: {e}")

def delete_rich_menu_alias(rich_menu_alias_id: str):
    try:
        messaging_api.delete_rich_menu_alias(rich_menu_alias_id)
        print(f"Deleted alias: {rich_menu_alias_id}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    rich_menu_id = create_rich_menus("./assets/schema.json")
    if rich_menu_id:
        create_rich_menu_alias("my-alias", rich_menu_id)
    #delete_rich_menu_alias("my-alias")
    #delete_rich_menu("richmenu-178877fa76f33106e2391ffd2878c5a5")

