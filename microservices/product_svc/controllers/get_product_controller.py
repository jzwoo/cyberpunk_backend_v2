from microservices.product_svc.dal.product_DAL import ProductDAL


async def get_product_controller(product_dal: ProductDAL, product_id: str):
    product = await product_dal.get_product(product_id)

    if product is None:
        raise ValueError("Product does not exist.")
    else:
        return product
