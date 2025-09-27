import time
import os
from linebot.v3.messaging import Configuration, ApiClient, MessagingApiBlob
from pprint import pprint
from dotenv import load_dotenv
from PIL import Image

load_dotenv(override=True, dotenv_path=".env")
access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
configuration = Configuration(access_token=access_token)


def get_richmenu_image(rich_menu_id: str):
    """Download and display LINE Rich menu images.
    Args:
        rich_menu_id: Rich menu ID
    """
    
    # Enter a context with an instance of the API client
    with ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = MessagingApiBlob(api_client)
        
        try:
            # Get rich menu image
            image_data = api_instance.get_rich_menu_image(rich_menu_id)
            print(f"Successfully downloaded rich menu image. Size: {len(image_data)} bytes")
            
            # Display the image using PIL without saving to file
            try:
                from io import BytesIO
                img = Image.open(BytesIO(image_data))
                print(f"Image size: {img.size}")
                print(f"Image mode: {img.mode}")
                img.show()
            except Exception as img_error:
                print(f"Error displaying image: {img_error}")
                
        except Exception as e:
            print("Exception when calling MessagingApiBlob->get_rich_menu_image: %s\n" % e)
        
if __name__ == "__main__":
    rich_menu_id="richmenu-595db7774db65aa1484bb2a8d44273f6"
    get_richmenu_image(rich_menu_id=rich_menu_id)