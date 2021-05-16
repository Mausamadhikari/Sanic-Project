from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

from src.allocation.domain.model import Batch, Product


class CreateBatch(BaseModel):
    sku_id: int
    purchase_order: int
    quantity: int
    material_handle: int
    manufactured_date: datetime
    expiry_date: datetime


class BatchCommand(BaseModel):
    batch: Batch


class UpdadteBatchQuantity(BatchCommand):
    quantity: int


class UpdadteBatchPurchaseOrder(BatchCommand):
    purchase_order: int


# def delete_batch(id_:int):
#     repo = BatchRepository()
#     batch = repo.get(id_)

# class DeleteBatch(BatchCommand):
#     id_ : int


class AddProduct(BaseModel):
    category: int
    name: str
    description: str
    slug: HttpUrl
    brand: str
    status: bool
    updated_date: Optional[datetime]


class ProductCommand(BaseModel):
    product: Product


class UpdateProduct(ProductCommand):
    category: int
    name: str
    description: str
    slug: HttpUrl
    brand: str
    status: bool
    updated_date: Optional[datetime]


class AddCategory(BaseModel):
    name: str
    sub_category: int
