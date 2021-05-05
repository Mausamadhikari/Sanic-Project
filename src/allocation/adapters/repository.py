from src.allocation.domain.model import Product, Batch, Category


from typing import List, Dict
from uuid import UUID

from randomthings.app import data_product_list, data_batch_list, data_category


# async def update_values(model: List[Dict], values: Dict):
#     """
#     Function to update values in all models
#     """
#     for i in range(len(model) + 1):
#         if model[i]["id_"] == values.id_:
#             model[i].update(values)
#     return model[i]


# async def get_values(self: List[Dict], values: Dict):
#     """
#     Function to update values in all models
#     """
#     for i in range(len(self) + 1):
#         if self[i]["id_"] == values.id_:
#             return self.dict()


# productrepository


class Productrepository:
    # Product model add , update and delete operations
    async def get_product(self, id_: Product.id_) -> Product:
        # get matching dictionary from static product list
        # construct domain model from matched
        # return product
        product = {}
        if id_ in data_product_list[id_]:
            product = data_product_list[id_]
        return Product.construct({product})

    # def get_all(self):
    #     return list(map(lambda item: item[1], self.items))

    async def add_product(self, model: Product):
        values = {
            "id_": model.id_,
            "category": model.category,
            "name": model.name,
            "description": model.description,
            "slug": model.slug,
            "brand": model.brand,
            "status": model.status,
            "updated_date": model.updated_date,
        }
        await model.append(values)

    async def update_product(self, model: Product) -> None:
        values = {
            "id_": model.id_,
            "category": model.category,
            "name": model.name,
            "description": model.description,
            "slug": model.slug,
            "brand": model.brand,
            "status": model.status,
            "updated_date": model.updated_date,
        }
        for i in range(len(self) + 1):
            if self[i]["id_"] == values.id_:
                await self[i].update(values)

    async def delete_product(self, model: Product):
        if self.id_ in model.id_:
            # can pop or use del
            del model.id_


class Batchrepository:
    # batch model add,update and delete operations
    async def get_batch(self, id_: UUID) -> Batch:
        # get matching dictionary from static product list
        # construct domain model from matched
        # return product
        batch = {}
        if id_ in data_batch_list[id_]:
            batch = data_batch_list[id_]
        return Batch.construct({batch})

    async def add_batch(self, model: Product):
        values = {
            "id_": model.id_,
            "sku_id_": model.sku_id_,
            "purchase_order": model.purchase_order,
            "material_handle": model.material_handle,
            "manufactured_date": model.manufactured_date,
            "expiry_date": model.expiry_date,
        }
        await model.append(values)

    async def update_batch(self, model: Batch):
        values = {
            "id_": model.id_,
            "sku_id_": model.sku_id_,
            "purchase_order": model.purchase_order,
            "material_handle": model.material_handle,
            "manufactured_date": model.manufactured_date,
            "expiry_date": model.expiry_date,
        }

        for i in range(len(self) + 1):
            if self[i]["id_"] == values.id_:
                await self[i].update(values)

    async def delete_batch(self, model: Batch):
        if self.id_ in model.id_:
            del model.id_
            return "{model.id_} is deleted successfully"


class Categoryrepository:
    # category model add,update and delete operations
    async def get_category(self, id_: UUID):
        # get matching dictionary from static product list
        # construct domain model from matched
        # return product
        category = {}
        if id_ in data_category[id_]:
            category = data_category[id_]
        return Category.construct({category})

    async def add_category(self, model: Product):
        values = {
            "id_": model.id_,
            "name": model.name,
            "sub_category": model.sub_category,
        }
        await model.append(values)

    async def update_category(self, model: Category):
        values = {
            "id_": model.id_,
            "name": model.name,
            "sub_category": model.sub_category,
        }
        for i in range(len(self) + 1):
            if self[i]["id_"] == values.id_:
                await self[i].update(values)

    async def delete_category(self, model: Category):
        if self.id_ in model.id_:
            del model.id_
            return "{model.id_} is deleted successfully"
