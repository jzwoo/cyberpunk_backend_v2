import uuid

from pydantic import EmailStr
from pymongo import ReturnDocument

from common.models.dal import DAL
from microservices.user_svc.models.user import UserIn


class UserDAL(DAL):
    __collection_name = "users"

    def __init__(self, db):
        super().__init__(db, self.__collection_name)

    async def get_user_by_email(self, email: EmailStr):
        return await self._get_item({"email": email})

    async def get_user_by_id(self, user_id: str):
        return await self._get_item_by_id(user_id)

    async def create_user(self, user: UserIn):
        return await self._create_item(user)

    async def update_user(self, user: UserIn, email: EmailStr):
        return await self._update_item(user, {"email": email})

    async def set_user_refresh_token(self, email: EmailStr, refresh_token: str):
        return await self._collection.find_one_and_update(
            {"email": email},
            {"$set": {"refresh_token": refresh_token}},
            return_document=ReturnDocument.AFTER,
        )

    async def unset_user_refresh_token(self, email: EmailStr):
        return await self._collection.find_one_and_update(
            {"email": email},
            {"$unset": {"refresh_token": ""}},
            return_document=ReturnDocument.AFTER,
        )
