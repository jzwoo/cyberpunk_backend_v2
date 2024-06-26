from fastapi.security import HTTPBasicCredentials

from microservices.user_svc.dal.user_DAL import UserDAL
from microservices.user_svc.utils.jwt_utils import (
    generate_refresh_token,
    generate_access_token,
)
from microservices.user_svc.utils.secret import is_password_valid


async def login_controller(user_dal: UserDAL, credentials: HTTPBasicCredentials):
    if (user := await user_dal.get_user(credentials.username)) is None:
        raise ValueError("Incorrect username")

    if not is_password_valid(
        plain_password=credentials.password, hashed_password=user.get("password", "")
    ):
        raise ValueError("Incorrect password")

    refresh_token = generate_refresh_token(user)
    access_token = generate_access_token(user)

    updated_user = await user_dal.set_user_refresh_token(
        user.get("username"), refresh_token
    )

    return access_token, refresh_token, updated_user
