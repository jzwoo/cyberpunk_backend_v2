import jwt
from fastapi import APIRouter, HTTPException, Request, Response, Depends
from fastapi.security import (
    HTTPBasicCredentials,
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from pydantic import ValidationError

from db.db import get_db
from user_svc.controllers.auth.login_controller import login_controller
from user_svc.controllers.auth.logout_controller import logout_controller
from user_svc.controllers.auth.refresh_controller import refresh_controller
from user_svc.controllers.auth.register_controller import register_controller
from user_svc.dal.user_DAL import UserDAL
from user_svc.models.user import UserIn, UserOut, LoginSuccessResponse
from user_svc.utils.jwt_utils import decode_access_token, decode_refresh_token

auth = APIRouter()

user_dal = UserDAL(db=get_db())

auth_scheme = HTTPBearer()

tags = ["Auth"]


@auth.post(
    "/api/v1/register",
    response_description="Register",
    response_model=UserOut,
    tags=tags,
)
async def register(user: UserIn):
    try:
        return await register_controller(user_dal, user)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=f"Duplicate information: {e}")


@auth.post(
    "/api/v1/login",
    response_description="Login",
    response_model=LoginSuccessResponse,
    tags=tags,
)
async def login(credentials: HTTPBasicCredentials, response: Response):
    try:
        access_token, refresh_token, user = await login_controller(
            user_dal, credentials
        )

        # set cookie in the response
        response.set_cookie(
            key="jwt",
            value=refresh_token,
            max_age=24 * 60 * 60 * 1000,
            httponly=True,
            samesite="strict",
        )

        return LoginSuccessResponse(user=UserOut(**user), access_token=access_token)
    except ValueError as e:
        raise HTTPException(status_code=401)


@auth.post(
    "/api/v1/logout",
    response_description="Logout",
    tags=tags,
)
async def logout(
    response: Response, credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)
):
    try:
        requester = decode_access_token(credentials.credentials)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except ValidationError:
        raise HTTPException(status_code=401, detail="Invalid token")

    await logout_controller(user_dal, requester.username)

    # delete cookie from response
    response.delete_cookie("jwt")


@auth.get(
    "/api/v1/refresh",
    response_description="Refresh Token",
    response_model=LoginSuccessResponse,
    tags=tags,
)
async def refresh(request: Request, response: Response):
    cookies = request.cookies

    if cookies is None or "jwt" not in cookies:
        raise HTTPException(status_code=401)

    refresh_token = cookies.get("jwt")

    try:
        requester = decode_refresh_token(refresh_token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except ValidationError:
        raise HTTPException(status_code=401, detail="Invalid token")

    access_token, refresh_token, user = await refresh_controller(
        user_dal, requester.username
    )

    # set cookie in the response
    response.set_cookie(
        key="jwt",
        value=refresh_token,
        max_age=24 * 60 * 60 * 1000,
        httponly=True,
        samesite="strict",
    )

    return LoginSuccessResponse(user=UserOut(**user), access_token=access_token)
