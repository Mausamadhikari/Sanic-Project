from pydantic import BaseModel, Field, HttpUrl, validator
from datetime import datetime
from pydantic.color import Color
from typing import Optional, Dict, Any
from uuid import UUID


class Batch(BaseModel):

    id_: UUID
    sku_id: int
    purchase_order: int
    material_handle: int
    manufactured_date: datetime
    expiry_date: datetime  # check whether

    @validator("manufactured_date")
    def manufactured_within_five_years(cls, manufactured_date):
        time_in_delta = datetime.now() - manufactured_date
        if not abs(time_in_delta.days) <= 5 * 365:
            raise ValueError("Must be manufactured not exceeding five years from now")
        return manufactured_date

    class Config:
        extra = "Forbid"
        allow_mutations = False
        title = "Batch"

    def update(self, mapping: Dict[str, Any]) -> Batch:
        return self.copy(update=mapping)

    # def add_order(self, order: Order) -> Batch:
    #     orders = set(self.orders)
    #     orders.add(order)
    #     return self.copy(update={"orders": tuple(orders)})


def batch_factory(
    id_: UUID,
    sku_id: int,
    purchase_order: int,
    material_handle: int,
    manufactured_date: datetime,
    expiry_date: datetime,
) -> Batch:
    return Batch(
        id_=id,
        sku_id=sku_id,
        purchase_order=purchase_order,
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
        extra = "Forbid"
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

    @validator("name")
    def check_name_length(cls, name):
        if len(name) < 3:
            raise ValueError("Name too short!!!")
        return name

    class Config:
        extra = "Forbid"
        allow_mutations = False
        title = "Product"

    def update(self, mapping: Dict[str, Any]) -> Product:
        return self.copy(update=mapping)


def product_factory(
    id_: UUID,
    category: UUID,
    name: str,
    description: str,
    slug: HttpUrl,
    brand: str,
    status: bool,
    updated_date: Optional[datetime] = None,
) -> Product:
    return Product(
        id_=id,
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
        extra = "Forbid"
        allow_mutations = False
        title = "Category"

    def update(self, mapping: Dict[str, Any]) -> Category:
        return self.copy(update=mapping)


def category_factory(
    id_: UUID,
    name: str,
    sub_category: UUID,
) -> Category:
    return Category(
        id_=id_,
        name=name,
        sub_category=sub_category,
    )


class Unit(BaseModel):
    id_: UUID
    total_unit: int
    label: str

    class Config:
        extra = "Forbid"
        allow_mutations = False
        title = "Unit"

    def update(self, mapping: Dict[str, Any]) -> Unit:
        return self.copy(update=mapping)


def unit_factory(
    id_: UUID,
    total_unit: int,
    label: str,
) -> Unit:
    return Unit(
        id_ - id_,
        total_unit=total_unit,
        label=label,
    )
