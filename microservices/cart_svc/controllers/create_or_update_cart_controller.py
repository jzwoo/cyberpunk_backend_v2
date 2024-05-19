from microservices.cart_svc.dal.cart_DAL import CartDAL
from microservices.cart_svc.models.cart import Cart


async def create_or_update_cart_controller(
    cart_dal: CartDAL, username: str, updated_cart: Cart
):
    return await cart_dal.create_or_update_cart(
        username=username, updated_cart=updated_cart
    )
