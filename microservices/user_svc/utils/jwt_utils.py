import os
import jwt
from datetime import datetime, timedelta

from microservices.user_svc.models.token import TokenIn

SECRET_KEY = os.environ.get("JWT_SECRET")
REFRESH_TOKEN_SECRET = os.environ.get("REFRESH_TOKEN_SECRET")


def generate_access_token(user):
    curr_datetime = datetime.utcnow()
    expiration_time_in_minutes = 5

    payload = {
        "uuid": user["uuid"],
        "username": user["username"],
        "name": user["name"],
        "iat": curr_datetime,
        "exp": curr_datetime + timedelta(minutes=expiration_time_in_minutes),
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def generate_refresh_token(user):
    curr_datetime = datetime.utcnow()
    expiration_time_in_minutes = 30

    payload = {
        "uuid": user["uuid"],
        "username": user["username"],
        "name": user["name"],
        "iat": curr_datetime,
        "exp": curr_datetime + timedelta(minutes=expiration_time_in_minutes),
    }

    token = jwt.encode(payload, REFRESH_TOKEN_SECRET, algorithm="HS256")
    return token


def decode_access_token(token: str) -> TokenIn:
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    # TODO: if token is from a different source. e.g. Google, Facebook, etc., need to do conversion first
    return TokenIn(**payload)


def decode_refresh_token(token) -> TokenIn:
    payload = jwt.decode(token, REFRESH_TOKEN_SECRET, algorithms=["HS256"])

    # TODO: if token is from a different source. e.g. Google, Facebook, etc., need to do conversion first
    return TokenIn(**payload)
