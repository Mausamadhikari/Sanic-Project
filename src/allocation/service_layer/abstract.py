from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime
from src.allocation.domain.model import Batch


class AddBatch(BaseModel):
    sku_id: int
    purchase_order: int
    quantity: int
    material_handle: int
    manufactured_date: datetime
    expiry_date: datetime


class UpdadteQuantity(BaseModel):
    quantity: int


class UpdadtePurchaseOrder(BaseModel):
    purchaseorder: int


class AddProduct(BaseModel):
    category: int
    name: str
    description: str
    slug: HttpUrl
    brand: str
    status: bool
    updated_date: Optional[datetime]


class UpdateProduct(BaseModel):
    category: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[HttpUrl] = None
    brand: Optional[str] = None
    status: Optional[bool] = None
    updated_date: Optional[datetime] = None


class AddCategory(BaseModel):
    name: str
    sub_category: int
