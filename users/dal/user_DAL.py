from pymongo import ReturnDocument

from models.common import DAL
from users.models.user import UserIn


class UserDAL(DAL):
    __collection_name = "users"

    def __init__(self, db):
        super().__init__(db, self.__collection_name)

    async def get_user(self, user_uuid: str):
        return await self._get_item_by_uuid(user_uuid)

    async def get_user_by_username(self, username: str):
        return await self._get_item({"username": username})

    async def create_user(self, user: UserIn):
        return await self._create_item(user)

    async def update_user(self, user_uuid: str, user_updates: dict):
        return await self._collection.find_one_and_update(
            {"uuid": user_uuid},
            {"$set": user_updates},
            return_document=ReturnDocument.AFTER,
        )
