from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from allocation.domain.model import Batch


class AddBatch(BaseModel):
    sku_id: UUID
    purchase_order: int
    quantity:int
    material_handle: int
    manufactured_date: datetime
    expiry_date: datetime


class BatchCommand(BaseModel):
    batch: Batch


class UpdadteBatchQuantity(BatchCommand):
    quantity: int



# def delete_batch(id_:UUID):
#     repo = BatchRepository()
#     batch = repo.get(id_)
    
# class DeleteBatch(BatchCommand):
#     id_ : UUID


class AddProduct(BaseModel):
    category: UUID
    name: str
    description: str
    slug: HttpUrl
    brand: str
    status: bool
    updated_date: Optional[datetime]


class AddCategory(BaseModel):
    name: str
    sub_category: UUID
