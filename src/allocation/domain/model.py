from __future__ import annotations
import uuid
from pydantic import BaseModel, Field, HttpUrl, validator
from datetime import datetime
from pydantic.color import Color
from typing import Optional, Dict, Any
from uuid import UUID, uuid4


class Batch(BaseModel):

    id_: UUID
    sku_id: UUID
    purchase_order: int
    quantity: int
    material_handle: int
    manufactured_date: datetime
    expiry_date: datetime  # check whether

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "Batch"

    def update(self, mapping: Dict[str, Any]) -> Batch:
        return self.copy(update=mapping)

    # def add_order(self, order: Order) -> Batch:
    #     orders = set(self.orders)
    #     orders.add(order)
    #     return self.copy(update={"orders": tuple(orders)})


def batch_factory(
    sku_id: int,
    purchase_order: int,
    quantity: int,
    material_handle: int,
    manufactured_date: datetime,
    expiry_date: datetime,
) -> Batch:
    return Batch(
        id_=uuid.uuid4(),
        sku_id=sku_id,
        purchase_order=purchase_order,
        quantity=quantity,
        material_handle=material_handle,
        manufactured_date=manufactured_date,
        expiry_date=expiry_date,
    )


class Sku(BaseModel):
    id_: UUID
    product: int
    color: Color
    size: str

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "SKU"


class Product(BaseModel):
    id_: UUID
    category: UUID
    name: str
    description: str
    slug: HttpUrl
    brand: str
    status: bool
    updated_date: Optional[datetime] = None

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "Product"

    def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)


def product_factory(
    category: UUID,
    name: str,
    description: str,
    slug: HttpUrl,
    brand: str,
    status: bool,
    updated_date: Optional[datetime] = None,
) -> Product:
    return Product(
        id_=uuid(),
        category=category,
        name=name,
        description=description,
        slug=slug,
        brand=brand,
        status=status,
        updated_date=updated_date,
    )


class Category(BaseModel):
    id_: UUID
    name: str
    sub_category: UUID

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "Category"

    def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)


def category_factory(
    id_: UUID,
    name: str,
    sub_category: UUID,
) -> Category:
    return Category(
        id_=uuid(),
        name=name,
        sub_category=sub_category,
    )


class Unit(BaseModel):
    id_: UUID
    total_unit: int
    label: str

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "Unit"

    def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)


def unit_factory(
    total_unit: int,
    label: str,
) -> Unit:
    return Unit(
        id_=uuid(),
        total_unit=total_unit,
        label=label,
    )
