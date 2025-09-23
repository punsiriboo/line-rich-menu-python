import sys
import os
import linebot
from linebot.v3.messaging import RichMenuRequest
from linebot.v3.messaging.rest import ApiException
from pprint import pprint

outer_lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(outer_lib_path)


configuration = linebot.v3.messaging.Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = linebot.v3.messaging.ApiClient(configuration) 
api_instance = linebot.v3.messaging.MessagingApiBlob(api_client)


def upload_richmenu_image(rich_menu_id:str, rich_menu_image_file: str):
    """Upload LINE Rich menu images.
    Args:
        rich_menu_id: Rich menu ID
        rich_menu_image_file: Rich menu images file path
    """

    with open(rich_menu_image_file, "r") as f:
        rich_menu_image = f.read()

    try:
        api_instance.set_rich_menu_image(rich_menu_id, body=rich_menu_image)
    except Exception as e:
        print("Exception when calling MessagingApiBlob->set_rich_menu_image: %s\n" % e)
        
if __name__ == "__main__":
    rich_menu_id="YOUR_RICH_MENU_ID"
    upload_richmenu_image(
        rich_menu_id=rich_menu_id,
        rich_menu_image_file="../rich-menu/schema.json"
    )