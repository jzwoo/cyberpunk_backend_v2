import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import ValidationError

from db.db import get_db
from microservices.user_svc.controllers.user.get_user_controller import (
    get_user_controller,
)
from microservices.user_svc.dal.user_DAL import UserDAL
from microservices.user_svc.models.user import UserOut
from microservices.user_svc.utils.jwt_utils import decode_access_token

user = APIRouter()

user_dal = UserDAL(db=get_db())

auth_scheme = HTTPBearer()

tags = ["User"]


@user.get(
    "/api/v1/users/{username}",
    response_description="Get user",
    response_model=UserOut,
    tags=tags,
)
async def get_user(
    username: str, credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)
):
    try:
        requester = decode_access_token(credentials.credentials)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except ValidationError:
        raise HTTPException(status_code=401, detail="Invalid token")

    if requester.username != username:
        raise HTTPException(status_code=403)

    try:
        return await get_user_controller(user_dal, username)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
