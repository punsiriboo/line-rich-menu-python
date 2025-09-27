import time
import os
from linebot.v3.messaging import Configuration, ApiClient, MessagingApiBlob
from pprint import pprint
from dotenv import load_dotenv

load_dotenv(override=True, dotenv_path=".env")
access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
configuration = Configuration(access_token=access_token)


def upload_richmenu_image(rich_menu_id: str, rich_menu_image_file: str):
    """Upload LINE Rich menu images.
    Args:
        rich_menu_id: Rich menu ID
        rich_menu_image_file: Rich menu images file path
    """
    
    # Enter a context with an instance of the API client
    with ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = MessagingApiBlob(api_client)
        
        try:
            # Pass file path directly with headers
            api_instance.set_rich_menu_image(rich_menu_id, rich_menu_image_file, _headers={'Content-Type': 'image/jpeg'})
            print(f"Successfully uploaded rich menu image: {rich_menu_image_file}")
        except Exception as e:
            print("Exception when calling MessagingApiBlob->set_rich_menu_image: %s\n" % e)
        
if __name__ == "__main__":
    rich_menu_id="richmenu-595db7774db65aa1484bb2a8d44273f6"
    upload_richmenu_image(
        rich_menu_id=rich_menu_id,
        rich_menu_image_file="rich-menu/richmenu.jpg"
    )