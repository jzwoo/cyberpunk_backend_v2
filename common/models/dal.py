from typing import Optional

import uuid
from pydantic import BaseModel
from pymongo import ReturnDocument


class DAL:
    __id_field = "id"

    def __init__(self, db, collection_name: str):
        self._collection = db[collection_name]

    async def _get_items(self, filters: Optional[dict] = None):
        return await self._collection.find(
            filter=filters, projection={"_id": False}
        ).to_list(length=None)

    async def _get_item_by_id(self, item_id: str):
        return await self._collection.find_one(
            filter={self.__id_field: item_id}, projection={"_id": False}
        )

    async def _get_item(self, filters: Optional[dict] = None):
        return await self._collection.find_one(
            filter=filters, projection={"_id": False}
        )

    async def _create_item(self, basemodel: BaseModel):
        new_model_json = basemodel.model_dump()
        # create the default id
        new_id = str(uuid.uuid4())
        new_model_json[self.__id_field] = new_id

        await self._collection.insert_one(new_model_json)
        return await self._collection.find_one(
            filter={self.__id_field: new_id}, projection={"_id": False}
        )

    async def _update_item(self, update: BaseModel, filters: Optional[dict] = None):
        update_model_json = update.model_dump()

        return await self._collection.find_one_and_update(
            filter=filters,
            update={"$set": update_model_json},
            projection={"_id": False},
            return_document=ReturnDocument.AFTER,
        )

    async def _delete_item_by_id(self, item_id: str):
        return await self._collection.find_one_and_delete(
            filter={self.__id_field: item_id}, projection={"_id": False}
        )

    async def _delete_item(self, filters: Optional[dict] = None):
        return await self._collection.find_one_and_delete(
            filter=filters, projection={"_id": False}
        )
