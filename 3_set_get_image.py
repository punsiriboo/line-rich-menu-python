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


def upload_richmenu_image(rich_menu_id: str, image_path: str):
    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        messaging_api_blob.set_rich_menu_image(
            rich_menu_id,
            body=image_bytes,
            _headers={"Content-Type": "image/jpeg"},
        )
        print(f"Uploaded: {image_path}")
    except Exception as e:
        print(f"Error: {e}")


def get_richmenu_image(rich_menu_id: str, show: bool = False):
    try:
        image_data = messaging_api_blob.get_rich_menu_image(rich_menu_id)
        img = Image.open(BytesIO(image_data))
        print(f"Downloaded: {len(image_data)} bytes, Size: {img.size}, Mode: {img.mode}")
        if show:
            img.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    rich_menu_id = "richmenu-ccdb12652964190503e5933af502dac5"
    upload_richmenu_image(
        rich_menu_id=rich_menu_id,
        image_path="./assets/richmenu.jpg",
    )
    get_richmenu_image(rich_menu_id=rich_menu_id)
