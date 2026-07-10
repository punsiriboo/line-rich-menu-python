import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, RichMenuRequest
from linebot.v3.messaging.rest import ApiException

load_dotenv(override=True, dotenv_path="../.env")

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
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_rich_menus("../rich-menu/schema.json")