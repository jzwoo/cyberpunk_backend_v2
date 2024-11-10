from typing import Optional

from common.models.dal import DAL
from microservices.user_svc.models.cart import Cart


class CartDAL(DAL):
    __collection_name = "carts"

    def __init__(self, db):
        super().__init__(db, self.__collection_name)

    async def get_carts(self, query: Optional[dict] = None):
        return await self._get_items(query)

    async def get_cart(self, user_id: str):
        return await self._get_item({"user_id": user_id})

    async def create_cart(self, cart: Cart):
        return await self._create_item(cart)

    async def update_cart(self, user_id: str, updated_cart: Cart):
        return await self._update_item(
            update=updated_cart, filters={"user_id": user_id}
        )

    async def delete_cart(self, user_id: str):
        return await self._delete_item({"user_id": user_id})
