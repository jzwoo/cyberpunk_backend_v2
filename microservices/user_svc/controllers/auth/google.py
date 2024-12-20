import os

from google.oauth2 import id_token
from google.auth.transport import requests


async def verify_id_token(access_token: str):
    try:
        return id_token.verify_oauth2_token(
            access_token, requests.Request(), os.environ.get("GOOGLE_CLIENT_ID")
        )
    except ValueError:
        raise ValueError("Invalid token")
