from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import List, Optional

from src.allocation.domain.model import Batch, Product


class Command(BaseModel):
    pass


class CreateBatch(Command):
    sku_id: int
    purchase_quantity: int
    quantity: int
    material_handle: int
    manufactured_date: datetime
    expiry_date: datetime


class Allocate(Command):
    sku_id: int
    qty: int


class BatchCommand(Command):
    batch: Batch


class UpdadteBatchQuantity(BatchCommand):
    quantity: int


class UpdadteBatchPurchaseQuantity(BatchCommand):
    purchase_quantity: int


# def delete_batch(id_:int):
#     repo = BatchRepository()
#     batch = repo.get(id_)

# class DeleteBatch(BatchCommand):
#     id_ : int


class CreateProduct(Command):
    category: int
    name: str

    description: str
    slug: HttpUrl
    brand: str
    status: bool
    updated_date: Optional[datetime]


class ProductCommand(Command):
    product: Product


class UpdateProduct(ProductCommand):
    category: int
    name: str
    description: str
    slug: HttpUrl
    brand: str
    status: bool
    updated_date: Optional[datetime]


class UpdateProductCategory(ProductCommand):
    category: int


class UpdateProductName(ProductCommand):
    name: str


class UpdateProductDescription(ProductCommand):
    description: str


class UpdateProductSlug(ProductCommand):
    slug: HttpUrl


class UpdateProductBrand(ProductCommand):
    brand: str


class UpdateProductStatus(ProductCommand):
    status: bool


class UpdateProductUpdatedDate(ProductCommand):
    updated_date: Optional[datetime]


class CreateCategory(Command):
    name: str
    sub_category: int
