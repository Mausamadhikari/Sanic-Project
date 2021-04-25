from src.models import ProductModel, BatchModel, CategoryModel


from typing import List, Dict

from ..app import data_product_list, data_batch_list, data_category


async def update_values(self: List[Dict], values: Dict):
    """
        Function to update values in all models
        """
    for i in range(len(self)+1):
        if self[i]['id'] == values.id:
            product_with_id = self[i]
            product_with_id.update(values)

#productrepository
class Batchrepository:
    # Product model add , update and delete operations

    async def add_product(self, model: ProductModel):
        values = {
            "id": model.id,
            "category": model.category,
            "name": model.name,
            "description": model.description,
            "slug": model.slug,
            "brand": model.brand,
            "status": model.status,
            "updated_date": model.updated_date,
        }
        await model.append(values)

    async def update_product(self, model: ProductModel):
        values = {
            "id": model.id,
            "category": model.category,
            "name": model.name,
            "description": model.description,
            "slug": model.slug,
            "brand": model.brand,
            "status": model.status,
            "updated_date": model.updated_date,
        }
        await model.update_values(values)

    async def delete_product(self, model: ProductModel):
        if self.id in model.id:
            del model.id
            return "{model.id} is deleted successfully"

    # batch model add,update and delete operations

    async def add_batch(self, model: ProductModel):
        values = {
            "id": model.id,
            "sku_id": model.sku_id,
            "purchase_order": model.purchase_order,
            "material_handle": model.material_handle,
            "manufactured_date": model.manufactured_date,
            "expiry_date": model.expiry_date,
        }
        await data_product_list.append(values)

    async def update_batch(self, model: BatchModel):
        values = {
            "id": model.id,
            "sku_id": model.sku_id,
            "purchase_order": model.purchase_order,
            "material_handle": model.material_handle,
            "manufactured_date": model.manufactured_date,
            "expiry_date": model.expiry_date,
        }

        await model.update_values(values)

    async def delete_batch(self, model: BatchModel):
        if self.id in model.id:
            del model.id
            return "{model.id} is deleted successfully"

    # category model add,update and delete operations

    async def add_category(self, model: ProductModel):
        values = {
            'id': model.id,
            'name': model.name,
            'sub_category': model.sub_category,
        }
        await data_product_list.append(values)

    async def update_category(self, model: CategoryModel):
        values = {
            'id': model.id,
            'name': model.name,
            'sub_category': model.sub_category,
        }
        await model.update_values(values)

    async def delete_category(self, model: CategoryModel):
        if self.id in model.id:
            del model.id
            return "{model.id} is deleted successfully"
