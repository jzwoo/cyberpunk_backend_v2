from cart_svc.dal.cart_DAL import CartDAL
from cart_svc.models.cart import Cart


async def create_or_get_cart_controller(cart_dal: CartDAL, username: str):
    # creates a new cart if the current user does not have one
    if (user_cart := await cart_dal.get_cart(username)) is None:
        user_cart = await cart_dal.create_or_update_cart(
            username, Cart(username=username)
        )

    return user_cart
