from src.allocation.domain import model
from src.allocation.domain.command import (
    CreateBatch,
    AddCategory,
    BatchCommand,
    UpdadteBatchQuantity,
)


def add_batch(cmd: CreateBatch) -> model.Batch:
    return model.batch_factory(
        sku_id=cmd.sku_id,
        purchase_order=cmd.purchase_order,
        quantity=cmd.quantity,
        material_handle=cmd.material_handle,
        manufactured_date=cmd.manufactured_date,
        expiry_date=cmd.expiry_date,
    )


async def update_batch(cmd: BatchCommand) -> model.Batch:
    if isinstance(cmd, UpdadteBatchQuantity):
        return cmd.batch.update({"quantity": cmd.quantity})


async def add_product(cmd: CreateBatch) -> model.Product:
    return model.product_factory(
        category=cmd.category,
        name=cmd.name,
        description=cmd.description,
        slug=cmd.slug,
        brand=cmd.brand,
        status=cmd.status,
        updated_date=cmd.updated_date,
    )


async def add_category(cmd: AddCategory) -> model.Category:
    return model.category_factory(
        name=cmd.name,
        sub_category=cmd.sub_category,
    )


# import command
# from source.domain.model import Shipment, Order, OrderDetail,
# from source.domain import model

# async def add_shipment(cmd:command.AddShipment)

# async def add_batch(cmd: command.AddBatch) -> model.Batch:
#     return model.batch_factory()  # pass factory argu
