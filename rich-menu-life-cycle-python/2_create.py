import os
from pprint import pprint
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, RichMenuRequest
from linebot.v3.messaging.rest import ApiException

load_dotenv(override=True, dotenv_path=".env")

configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration) 
api_instance = MessagingApi(api_client)


def create_rich_menus(rich_menu_file: str):
    """Creates LINE Rich menu based on a JSON schema file.

    Args:
        rich_menu_file: JSON schema file path
    """
    try:
        with open(rich_menu_file, "r") as f:
            richmenu_json = f.read()

        rich_menu_request = RichMenuRequest.from_json(richmenu_json)
        api_response = api_instance.create_rich_menu(rich_menu_request=rich_menu_request) # Corrected parameter name
        print(f"Successfully created rich menu from {rich_menu_file}:")
        pprint(api_response)

        rich_menu_id = api_response.rich_menu_id
        print(f"Rich menu ID: {rich_menu_id}")
        
    except FileNotFoundError:
        print(f"Error: Rich menu JSON file not found: {rich_menu_file}")
    except ApiException as e:
        print(f"Error creating rich menu from {rich_menu_file}: {e}")
    except Exception as e:  # Catch other potential errors
            print(f"An unexpected error occurred processing {rich_menu_file}: {e}")

if __name__ == "__main__":
    create_rich_menus("rich-menu/schema.json")