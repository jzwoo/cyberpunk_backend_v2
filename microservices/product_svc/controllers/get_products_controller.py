from microservices.product_svc.dal.product_DAL import ProductDAL


async def get_products_controller(product_dal: ProductDAL, query: dict = None):
    return await product_dal.get_products(query)
