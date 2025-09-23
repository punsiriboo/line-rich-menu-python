import sys
import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApiBlob

load_dotenv(override=True, dotenv_path=".env")


configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration) 
api_instance = MessagingApiBlob(api_client)

load_dotenv(override=True, dotenv_path=".env")

def upload_richmenu_image(rich_menu_id:str, rich_menu_image_file: str):
    """Upload LINE Rich menu images.
    Args:
        rich_menu_id: Rich menu ID
        rich_menu_image_file: Rich menu images file path
    """

    try:
        with open(rich_menu_image_file, "rb") as f:
            api_instance.set_rich_menu_image(
                rich_menu_id=rich_menu_id,
                body=f
            )
    except Exception as e:
        print("Exception when calling MessagingApiBlob->set_rich_menu_image: %s\n" % e)
        
if __name__ == "__main__":
    rich_menu_id="richmenu-673913717d308be8e741786139158819"
    upload_richmenu_image(
        rich_menu_id=rich_menu_id,
        rich_menu_image_file="rich-menu/richmenu.jpg"
    )