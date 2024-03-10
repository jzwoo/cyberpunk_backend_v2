from models.common import DAL
from users.models.user import UserIn


class UserDAL(DAL):
    __collection_name = "users"

    def __init__(self, db):
        super().__init__(db, self.__collection_name)

    async def get_user(self, user_uuid: str):
        return await self._get_item(user_uuid)

    async def create_user(self, user: UserIn):
        return await self._create_item(user)
