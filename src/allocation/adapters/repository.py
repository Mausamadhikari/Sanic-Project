from typing import Dict, List
from src.allocation.domain.model import Product, Batch, Category
from src.lib.abstract_repository import AbstractRepository
import json

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
data_product_list = [
    {
        "id_": 1,
        "category": 1,
        "name": "HP inspiron 5000",
        "description": "This is i5 11th generation intel core Laptop with 8GB RAM",
        "slug": "https://guthib.com/mausamadhikari",
        "brand": "HP",
        "status": True,
        "updated_date": "2005-01-01T00:00",
    }
]
data_category = []
data_batch = []


class ProductRepository(AbstractRepository):
    # Product model add , update and delete operations
    def _get(self, id_: int) -> Product:
        # get matching dictionary from static product list
        # construct domain model from matched
        # return product
        product_ = {}
        for product in data_product_list:
            if product["id_"] == id_:
                product_ = product
        # [product for product in data_product_list if product["id_"] == id_]
        # next(product for product in data_product_list if product["id_"] == id_)
        # dict(filter(lambda product:product["id_"]==id_,data_product_list))
        # return Product.construct(product_)
        print("Getting Product from Repo", product_)
        return Product.construct(**product_)

    def _add(self, model: Product):
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
        print("from Repository", values)
        data_product_list.append(values)

    def update(self, id_: int, model: Product) -> None:
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
        # for i in range(len(self) + 1):

        #     if self[i]["id_"] == values.id_:
        #         self[i] = values
        # print(data_product_list)
        for product in data_product_list:
            if product["id_"] == id_:
                product.update(values)

    def delete(self, model: Product):
        if self.id_ in model.id_:
            # can pop or use del
            del model.id_


class BatchRepository(AbstractRepository):
    # batch model add,update and delete operations
    def _get(self, id_: int) -> Batch:
        # get matching dictionary from static product list
        # construct domain model from matched
        # return product
        # batch = {}
        for data in data_batch:
            if id_ == data["sku_id"]:
                print(data)
                return Batch.construct(**data)
        # with open("batch_file.json", "r+") as f:
        #     data_batch_list = json.load()
        #     if id_ in data_batch_list["id_"]:
        #         batch = data_batch_list
        #     else:
        #         batch is None
        # return Batch.construct(**batch)

    def _add(self, model: Batch):
        values = {
            "id_": model.id_,
            "sku_id": model.sku_id,
            "purchase_quantity": model.purchase_quantity,
            "quantity": model.quantity,
            "material_handle": model.material_handle,
            "manufactured_date": model.manufactured_date,
            "expiry_date": model.expiry_date,
        }
        data_batch.append(values)
        print(data_batch)
        with open("batch_file.json", "a+") as f:
            f.write(f"{values}\n")

    def update(self, model: Batch):
        values = {
            "id_": model.id_,
            "sku_id_": model.sku_id,
            "purchase_quantity": model.purchase_quantity,
            "quantity": model.quantity,
            "material_handle": model.material_handle,
            "manufactured_date": model.manufactured_date,
            "expiry_date": model.expiry_date,
        }
        with open("batch_file.json", "r+") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.seek(0)
            if data["id_"] == values["id_"]:
                data = values
                json.dump(data, jsonFile)
            jsonFile.truncate()

        # for i in range(len(self) + 1):
        #     if self[i]["id_"] == values.id_:
        #         self[i].update(values)

    def delete(self, model: Batch):
        if self.id_ in model.id_:
            del model.id_
            return "{model.id_} is deleted successfully"


class CategoryRepository(AbstractRepository):
    # category model add,update and delete operations
    def _get(self, id_: int):
        # get matching dictionary from static product list
        # construct domain model from matched
        # return product
        category = {}
        if id_ in data_category[id_]:
            category = data_category[id_]
        return Category.construct({category})

    def _add(self, model: Category):
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
