class ProductDAL:
    __collection_name = "products"

    def __init__(self, db):
        self.__collection = db[self.__collection_name]

    async def get_products(self, query: dict = None):
        return await self.__collection.find(query).to_list(length=None)
