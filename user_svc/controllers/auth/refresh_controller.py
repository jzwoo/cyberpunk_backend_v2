from user_svc.dal.user_DAL import UserDAL
from user_svc.utils.jwt_utils import generate_refresh_token, generate_access_token


async def refresh_controller(user_dal: UserDAL, username: str):
    if (user := await user_dal.get_user(username)) is None:
        raise ValueError("Incorrect username")

    refresh_token = generate_refresh_token(user)
    access_token = generate_access_token(user)

    updated_user = await user_dal.set_user_refresh_token(username, refresh_token)

    return access_token, refresh_token, updated_user
