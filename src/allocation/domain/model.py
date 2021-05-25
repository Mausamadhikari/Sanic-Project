from __future__ import annotations
from pydantic import BaseModel, Field, HttpUrl, validator
from datetime import datetime
from pydantic.color import Color
from typing import Optional, Dict, Any
from src.allocation.domain import events
from src.lib.id_generator import id_gen
from typing import List


class OrderLine(BaseModel):
    sku_id: int
    qty: int

    def __hash__(self):
        return hash(self.sku_id)


def Orderline_factory(sku_id: int, qty: int) -> OrderLine:
    return OrderLine(orderid=id_gen(), sku_id=sku_id, qty=qty)


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

    def __hash__(self):
        return hash(self.id_)

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
    purchase_quantity: int
    quantity: int
    material_handle: int
    manufactured_date: datetime
    expiry_date: datetime  # check whether
    allocations = set()
    events: Optional[List]

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "Batch"

    def __eq__(self, other: Batch):
        if not isinstance(other, Batch):
            return False
        return other.id_ == self.id_

    def __gt__(self, other: Batch):
        if self.expiry_date is None:
            return False
        if other.expiry_date is None:
            return True
        return self.expiry_date > other.expiry_date

    def __lt__(self, other: Batch):
        if self.expiry_date is None:
            return False
        if other.expiry_date is None:
            return True
        return self.expiry_date < other.expiry_date

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self.allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self.allocations:
            self.allocations.remove(line)

    def deallocate_one(self) -> OrderLine:
        return self.allocations.pop()

    @property
    def allocated_quantity(self) -> int:
        return int(sum(line.qty for line in self.allocations))

    @property
    def available_quantity(self) -> int:
        return int(self.purchase_quantity) - int(self.allocated_quantity)

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku_id == line.sku_id and self.available_quantity >= line.qty

    def __hash__(self):
        return hash(self.id_)

    def update(self, mapping: Dict[str, Any]) -> Batch:
        return self.copy(update=mapping)

    # def add_order(self, order: Order) -> Batch:
    #     orders = set(self.orders)
    #     orders.add(order)
    #     return self.copy(update={"orders": tuple(orders)})


def batch_factory(
    sku_id: int,
    purchase_quantity: int,
    quantity: int,
    material_handle: int,
    manufactured_date: datetime,
    expiry_date: datetime,
) -> Batch:
    return Batch(
        id_=id_gen(),
        sku_id=sku_id,
        purchase_quantity=purchase_quantity,
        quantity=quantity,
        material_handle=material_handle,
        manufactured_date=manufactured_date,
        expiry_date=expiry_date,
        events=[],
    )


async def allocate(batch: Batch, line: OrderLine) -> str:
    try:
        batch = next(b for b in sorted(batch) if b.can_allocate(line))
        batch.allocate(line)

        batch.events.append(
            events.Allocated(
                sku=line.sku_id,
                qty=line.qty,
                batchref=batch.id_,
            )
        )
        return batch.reference
    except StopIteration:
        batch.events.append(events.OutOfStock(line.sku))
        return None


async def change_batch_quantity(batch: Batch, ref: str, qty: int):
    batch = next(b for b in batch if b.id_ == ref)
    batch.purchase_quantity = qty
    while batch.available_quantity < 0:
        line = batch.deallocate_one()
        batch.events.append(events.Deallocated(line.orderid, line.sku, line.qty))


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
