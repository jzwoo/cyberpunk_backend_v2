import os
import jwt
from datetime import datetime, timedelta

from microservices.user_svc.models.token import Token
from microservices.user_svc.models.user import UserOut

SECRET_KEY = os.environ.get("JWT_SECRET")
REFRESH_TOKEN_SECRET = os.environ.get("REFRESH_TOKEN_SECRET")
ACCESS_TOKEN_EXPIRATION_DURATION = 1
REFRESH_TOKEN_EXPIRATION_DURATION = 30


def generate_access_token(user: UserOut):
    curr_datetime = datetime.utcnow()

    raw_token = Token(
        id=user.id,
        email=user.email,
        name=user.name,
        iss="cyberpunk",
        iat=curr_datetime,
        exp=curr_datetime + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_DURATION),
    )

    encoded_token = jwt.encode(raw_token.model_dump(), SECRET_KEY, algorithm="HS256")
    return encoded_token


def generate_refresh_token(user: UserOut):
    curr_datetime = datetime.utcnow()

    raw_token = Token(
        id=user.id,
        email=user.email,
        name=user.name,
        iss="cyberpunk",
        iat=curr_datetime,
        exp=curr_datetime + timedelta(minutes=REFRESH_TOKEN_EXPIRATION_DURATION),
    )

    encoded_token = jwt.encode(
        raw_token.model_dump(), REFRESH_TOKEN_SECRET, algorithm="HS256"
    )
    return encoded_token


def decode_access_token(encoded_token: str) -> Token:
    raw_token = jwt.decode(encoded_token, options={"verify_signature": False})
    # raw_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    return Token(**raw_token)


def decode_refresh_token(encoded_token: str) -> Token:
    raw_token = jwt.decode(encoded_token, options={"verify_signature": False})
    # raw_token = jwt.decode(token, REFRESH_TOKEN_SECRET, algorithms=["HS256"])

    return Token(**raw_token)
