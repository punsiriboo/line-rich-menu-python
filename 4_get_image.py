import os
from linebot.v3.messaging import Configuration, ApiClient, MessagingApiBlob
from pathlib import Path
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv(override=True, dotenv_path=Path(__file__).resolve().parent / ".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api_blob = MessagingApiBlob(api_client)

def get_richmenu_image(rich_menu_id: str):
    try:
        image_data = messaging_api_blob.get_rich_menu_image(rich_menu_id)
        img = Image.open(BytesIO(image_data))
        print(f"Downloaded: {len(image_data)} bytes, Size: {img.size}, Mode: {img.mode}")
        img.show()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    rich_menu_id="richmenu-595db7774db65aa1484bb2a8d44273f6"
    get_richmenu_image(rich_menu_id=rich_menu_id)
