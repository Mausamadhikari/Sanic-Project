from src.allocation.domain.model import Product, Batch, Category


from typing import List, Dict
from uuid import UUID

from randomthings.app import data_product_list, data_batch_list, data_category
import abc

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


# ProductRepository
class AbstractRepository(abc.ABC):
    def get(self):
        raise NotImplementedError

    def add(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError


class ProductRepository(AbstractRepository):
    # Product model add , update and delete operations
    # def get(self, id_: Product.id_) -> Product:
    #     # get matching dictionary from static product list
    #     # construct domain model from matched
    #     # return product
    #     product = {}
    #     if id_ in data_product_list[id_]:
    #         product = data_product_list[id_]
    #     return Product.construct(product)

    def add(self, model: Product):
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
        model.append(values)

    def update(self, model: Product) -> None:
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
            # if self[i]["id_"] == values.id_:
            self[i].update(values)

    def delete(self, model: Product):
        if self.id_ in model.id_:
            # can pop or use del
            del model.id_


class BatchRepository(AbstractRepository):
    # batch model add,update and delete operations
    def get(self, id_: UUID) -> Batch:
        # get matching dictionary from static product list
        # construct domain model from matched
        # return product
        batch = {}
        if id_ in data_batch_list[id_]:
            batch = data_batch_list[id_]
        return Batch.construct(batch)

    def add(self, model: Batch):
        values = {
            "id_": model.id_,
            "sku_id": model.sku_id,
            "purchase_order": model.purchase_order,
            "quantity": model.quantity,
            "material_handle": model.material_handle,
            "manufactured_date": model.manufactured_date,
            "expiry_date": model.expiry_date,
        }
        #
        with open("file.json", "a+") as f:
            f.write(f"{values}\n")

    def update(self, model: Batch):
        values = {
            "id_": model.id_,
            "sku_id_": model.sku_id_,
            "purchase_order": model.purchase_order,
            "quantity": model.quantity,
            "material_handle": model.material_handle,
            "manufactured_date": model.manufactured_date,
            "expiry_date": model.expiry_date,
        }

        for i in range(len(self) + 1):
            if self[i]["id_"] == values.id_:
                self[i].update(values)

    def delete(self, model: Batch):
        if self.id_ in model.id_:
            del model.id_
            return "{model.id_} is deleted successfully"


class CategoryRepository(AbstractRepository):
    # category model add,update and delete operations
    def get(self, id_: UUID):
        # get matching dictionary from static product list
        # construct domain model from matched
        # return product
        category = {}
        if id_ in data_category[id_]:
            category = data_category[id_]
        return Category.construct({category})

    def add(self, model: Category):
        values = {
            "id_": model.id_,
            "name": model.name,
            "sub_category": model.sub_category,
        }
        model.append(values)

    def update(self, model: Category):
        values = {
            "id_": model.id_,
            "name": model.name,
            "sub_category": model.sub_category,
        }
        for i in range(len(self) + 1):
            if self[i]["id_"] == values.id_:
                self[i].update(values)

    def delete(self, model: Category):
        if self.id_ in model.id_:
            del model.id_
            return "{model.id_} is deleted successfully"
