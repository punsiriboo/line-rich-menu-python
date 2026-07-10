import os
from pathlib import Path
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

load_dotenv(override=True, dotenv_path=Path(__file__).resolve().parent / ".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)

def get_user_rich_menu(user_id: str):
    try:
        response = messaging_api.get_rich_menu_id_of_user(user_id)
        print(f"User {user_id} rich menu ID: {response.rich_menu_id}")
        return response.rich_menu_id
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    get_user_rich_menu("YOUR_USER_ID_HERE")
