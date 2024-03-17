from pymongo import ReturnDocument

from models.common import DAL
from users.models.user import UserIn


class UserDAL(DAL):
    __collection_name = "users"

    def __init__(self, db):
        super().__init__(db, self.__collection_name)

    async def get_user(self, username: str):
        return await self._get_item({"username": username})

    async def create_user(self, user: UserIn):
        return await self._create_item(user)

    async def set_user_refresh_token(self, username: str, refresh_token: str):
        return await self._collection.find_one_and_update(
            {"username": username},
            {"$set": {"refresh_token": refresh_token}},
            return_document=ReturnDocument.AFTER,
        )

    async def unset_user_refresh_token(self, username: str):
        return await self._collection.find_one_and_update(
            {"username": username},
            {"$unset": {"refresh_token": ""}},
            return_document=ReturnDocument.AFTER,
        )
