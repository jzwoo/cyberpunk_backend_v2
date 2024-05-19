from microservices.product_svc.dal.product_DAL import ProductDAL
from microservices.product_svc.models.product import ProductIn


async def create_product_controller(product_dal: ProductDAL, product: ProductIn):
    return await product_dal.create_product(product)
