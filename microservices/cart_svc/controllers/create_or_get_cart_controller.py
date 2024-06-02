from microservices.cart_svc.dal.cart_DAL import CartDAL
from microservices.cart_svc.models.cart import Cart


async def create_or_get_cart_controller(cart_dal: CartDAL, provider: str, user_id: str):
    # creates a new cart if the current user does not have one
    if (
        user_cart := await cart_dal.get_cart(provider=provider, user_id=user_id)
    ) is None:
        user_cart = await cart_dal.create_or_update_cart(
            provider, user_id, Cart(provider=provider, user_id=user_id)
        )

    return user_cart
