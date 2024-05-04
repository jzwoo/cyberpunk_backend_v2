from users.dal.user_DAL import UserDAL


async def get_user_controller(user_dal: UserDAL, username: str):
    user = await user_dal.get_user(username)

    if user is None:
        raise ValueError("User does not exist.")
    else:
        return user
