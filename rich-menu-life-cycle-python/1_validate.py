import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, RichMenuRequest
from linebot.v3.messaging.rest import ApiException

load_dotenv(override=True, dotenv_path="../.env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)

def validate_rich_menu(rich_menu_file: str):
    try:
        with open(rich_menu_file, "r") as f:
            rich_menu_request = RichMenuRequest.from_json(f.read())
        messaging_api.validate_rich_menu_object(rich_menu_request=rich_menu_request)
        print(f"Validated: {rich_menu_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    validate_rich_menu("../rich-menu/schema.json")