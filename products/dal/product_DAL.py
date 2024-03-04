import uuid
from products.models.product import ProductIn


class ProductDAL:
    __collection_name = "products"

    def __init__(self, db):
        self.__collection = db[self.__collection_name]

    async def get_products(self, query: dict = None):
        return await self.__collection.find(query).to_list(length=None)

    async def get_product(self, product_uuid: str):
        return await self.__collection.find_one({"uuid": product_uuid})

    async def create_product(self, product: ProductIn):
        new_product_json = product.model_dump()
        new_product_uuid = str(uuid.uuid4())
        new_product_json["uuid"] = new_product_uuid

        await self.__collection.insert_one(new_product_json)
        return await self.__collection.find_one({"uuid": new_product_uuid})

    async def delete_product(self, product_uuid: str):
        return await self.__collection.find_one_and_delete({"uuid": product_uuid})
