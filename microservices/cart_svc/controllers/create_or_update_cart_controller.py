from microservices.cart_svc.dal.cart_DAL import CartDAL
from microservices.cart_svc.models.cart import Cart


async def create_or_update_cart_controller(
    cart_dal: CartDAL, provider: str, user_id: str, updated_cart: Cart
):
    return await cart_dal.create_or_update_cart(
        provider, user_id, updated_cart=updated_cart
    )
