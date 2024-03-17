import uuid
from pydantic import BaseModel


class UUID(BaseModel):
    uuid: str


class DAL:
    def __init__(self, db, collection_name: str):
        self._collection = db[collection_name]

    async def _get_items(self, query: dict = None):
        return await self._collection.find(query).to_list(length=None)

    async def _get_item_by_uuid(self, uuid: str):
        return await self._collection.find_one({"uuid": uuid})

    async def _get_item(self, query: dict = None):
        return await self._collection.find_one(query)

    async def _create_item(self, basemodel: BaseModel):
        new_model_json = basemodel.model_dump()
        new_uuid = str(uuid.uuid4())
        new_model_json["uuid"] = new_uuid

        await self._collection.insert_one(new_model_json)
        return await self._collection.find_one({"uuid": new_uuid})

    async def _delete_item(self, uuid: str):
        return await self._collection.find_one_and_delete({"uuid": uuid})
