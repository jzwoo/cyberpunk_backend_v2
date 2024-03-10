from fastapi import APIRouter, HTTPException

from db.db import get_db
from users.dal.user_DAL import UserDAL

auth = APIRouter()

product_dal = UserDAL(db=get_db())

tags = ["Auth"]


@auth.get(
    "/api/v1/register",
    response_description="Register",
    # response_model=list[ProductOut],
    tags=tags,
)
async def login():
    return "login"


@auth.get(
    "/api/v1/login",
    response_description="Login",
    # response_model=list[ProductOut],
    tags=tags,
)
async def register():
    return "register"


@auth.get(
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
