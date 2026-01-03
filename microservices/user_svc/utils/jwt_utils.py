import os
import jwt
from datetime import datetime, timedelta

from microservices.user_svc.models.token import Token
from microservices.user_svc.models.user import UserOut

SECRET_KEY = os.environ.get("JWT_SECRET")
REFRESH_TOKEN_SECRET = os.environ.get("REFRESH_TOKEN_SECRET")
ACCESS_TOKEN_EXPIRATION_SECONDS = 10
REFRESH_TOKEN_EXPIRATION_SECONDS = 60


def generate_access_token(user: UserOut):
    curr_datetime = datetime.utcnow()

    raw_token = Token(
        id=user.id,
        email=user.email,
        name=user.name,
        iss="cyberpunk",
        iat=curr_datetime,
        exp=curr_datetime + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_SECONDS),
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
        exp=curr_datetime + timedelta(minutes=REFRESH_TOKEN_EXPIRATION_SECONDS),
    )

    encoded_token = jwt.encode(
        raw_token.model_dump(), REFRESH_TOKEN_SECRET, algorithm="HS256"
    )
    return encoded_token


def decode_access_token(encoded_token: str) -> Token:
    # access token will be verified by gateway, application layer does not need to verify
    raw_token = jwt.decode(encoded_token, options={"verify_signature": False})

    return Token(**raw_token)


def decode_refresh_token(encoded_token: str) -> Token:
    # refresh token must be verified at application layer
    raw_token = jwt.decode(encoded_token, REFRESH_TOKEN_SECRET, options={"verify_signature": True},
                           algorithms=["HS256"])

    return Token(**raw_token)
