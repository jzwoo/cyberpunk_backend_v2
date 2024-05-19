from user_svc.dal.user_DAL import UserDAL


async def logout_controller(user_dal: UserDAL, username: str):
    if await user_dal.get_user(username) is not None:
        await user_dal.unset_user_refresh_token(username)
