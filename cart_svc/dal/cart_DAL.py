from cart_svc.models.cart import Cart
from common.models.dal import DAL


class CartDAL(DAL):
    __collection_name = "carts"

    def __init__(self, db):
        super().__init__(db, self.__collection_name)

    async def get_carts(self, query: dict = None):
        return await self._get_items(query)

    async def get_cart(self, username: str):
        return await self._get_item({"username": username})

    async def create_or_update_cart(self, username: str, updated_cart: Cart):
        return await self._update_item(
            update=updated_cart, query={"username": username}, upsert=True
        )

    async def delete_cart(self, username: str):
        return await self._delete_item({"username": username})
