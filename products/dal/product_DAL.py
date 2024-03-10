from models.common import DAL
from products.models.product import ProductIn


class ProductDAL(DAL):
    __collection_name = "products"

    def __init__(self, db):
        super().__init__(db, self.__collection_name)

    async def get_products(self, query: dict = None):
        return await self._get_items(query)

    async def get_product(self, product_uuid: str):
        return await self._get_item(product_uuid)

    async def create_product(self, product: ProductIn):
        return await self._create_item(product)

    async def delete_product(self, product_uuid: str):
        return await self._delete_item(product_uuid)
