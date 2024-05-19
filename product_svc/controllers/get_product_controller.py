from product_svc.dal.product_DAL import ProductDAL


async def get_product_controller(product_dal: ProductDAL, product_uuid: str):
    product = await product_dal.get_product(product_uuid)

    if product is None:
        raise ValueError("Product does not exist.")
    else:
        return product
