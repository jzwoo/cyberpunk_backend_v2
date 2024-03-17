from fastapi import APIRouter, HTTPException, Response
from fastapi.security import HTTPBasicCredentials

from db.db import get_db
from users.controllers.login_controller import login_controller
from users.controllers.register_controller import register_controller
from users.dal.user_DAL import UserDAL
from users.models.user import UserIn, UserOut, LoginSuccessResponse

auth = APIRouter()

user_dal = UserDAL(db=get_db())

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
    # response_model=list[ProductOut],
    tags=tags,
)
async def logout():
    return "logout"


@auth.get(
    "/api/v1/refresh",
    response_description="Refresh Token",
    # response_model=list[ProductOut],
    tags=tags,
)
async def refresh():
    return "refresh"
