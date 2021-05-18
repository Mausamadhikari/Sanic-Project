from __future__ import annotations
from pydantic import BaseModel, Field, HttpUrl, validator
from datetime import datetime
from pydantic.color import Color
from typing import Optional, Dict, Any
from allocation.domain import events
from src.lib.id_generator import id_gen
from typing import List


class Product(BaseModel):
    id_: int
    category: int
    name: str
    description: str
    slug: HttpUrl
    brand: str
    status: bool
    updated_date: Optional[datetime]
    events: Optional[List]

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "Product"

    def update(self, mapping: Dict[str, Any]) -> Product:
        return self.copy(update=mapping)


def product_factory(
    category: int,
    name: str,
    description: str,
    slug: HttpUrl,
    brand: str,
    status: bool,
    updated_date: Optional[datetime] = None,
) -> Product:
    return Product(
        id_=id_gen(),
        category=category,
        name=name,
        description=description,
        slug=slug,
        brand=brand,
        status=status,
        updated_date=updated_date,
        events=[],
    )


class Batch(BaseModel):

    id_: int
    sku_id: int
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
        id_=id_gen(),
        sku_id=sku_id,
        purchase_order=purchase_order,
        quantity=quantity,
        material_handle=material_handle,
        manufactured_date=manufactured_date,
        expiry_date=expiry_date,
    )


class Sku(BaseModel):
    id_: int
    product: int
    color: Color
    size: str

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "SKU"


class Category(BaseModel):
    id_: int
    name: str
    sub_category: int

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "Category"

    def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)


def category_factory(
    id_: int,
    name: str,
    sub_category: int,
) -> Category:
    return Category(
        id_=id_gen(),
        name=name,
        sub_category=sub_category,
    )


class Unit(BaseModel):
    id_: int
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
        id_=id_gen(),
        total_unit=total_unit,
        label=label,
    )
