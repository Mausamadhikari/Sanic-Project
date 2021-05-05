from pydantic import BaseModel,HttpUrl
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4


class AddBatch(BaseModel):
    sku_id: UUID
    purchase_order: int
    material_handle: int
    manufactured_date: datetime
    expiry_date: datetime

class AddProduct(BaseModel):
    id_: UUID
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
