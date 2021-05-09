from pydantic import BaseModel,HttpUrl
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from src.allocation.domain.model import Batch


class AddBatch(BaseModel):
    sku_id: UUID
    purchase_order: int
    quantity:int
    material_handle: int
    manufactured_date: datetime
    expiry_date: datetime


class BatchCommand(BaseModel):
    batch: Batch


class UpdadteQuantity(BatchCommand):
    quantity: int



class AddProduct(BaseModel):
    category: UUID
    name: str
    description: str
    slug: HttpUrl
    brand: str
    status: bool
    updated_date: Optional[datetime]


class AddCategory(BaseModel):
    id_: UUID
    name: str
    sub_category: UUID
