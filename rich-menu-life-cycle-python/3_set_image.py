import os
from linebot.v3.messaging import Configuration, ApiClient, MessagingApiBlob
from dotenv import load_dotenv

load_dotenv(override=True, dotenv_path=".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api_blob = MessagingApiBlob(api_client)

def upload_richmenu_image(rich_menu_id: str, image_path: str):
    try:
        messaging_api_blob.set_rich_menu_image(rich_menu_id, image_path, _headers={'Content-Type': 'image/jpeg'})
        print(f"Uploaded: {image_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    rich_menu_id="richmenu-595db7774db65aa1484bb2a8d44273f6"
    upload_richmenu_image(
        rich_menu_id=rich_menu_id,
        rich_menu_image_file="rich-menu/richmenu.jpg"
    )