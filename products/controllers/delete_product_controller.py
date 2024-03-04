from products.dal.product_DAL import ProductDAL


async def delete_product_controller(product_dal: ProductDAL, product_uuid: str):
    product = await product_dal.delete_product(product_uuid)

    if product is None:
        raise ValueError("Product does not exist.")
