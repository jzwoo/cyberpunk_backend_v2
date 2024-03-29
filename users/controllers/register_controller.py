from users.dal.user_DAL import UserDAL
from users.models.user import UserIn
from users.utils.secret import hash_password


async def register_controller(user_dal: UserDAL, user_in: UserIn):
    if await user_dal.get_user(user_in.username) is not None:
        raise ValueError("Duplicate username.")

    # salt and hash password
    user_in.password = hash_password(user_in.password)

    return await user_dal.create_user(user_in)
