from src.allocation.domain import model
from src.allocation.domain.command import AddBatch, AddCategory


async def add_batch(cmd: AddBatch) -> model.Batch:
    return model.batch_factory(
        id_=cmd.id_,
        sku_id=cmd.sku_id,
        purchase_order=cmd.purchase_order,
        material_handle=cmd.material_handle,
        manufactured_date=cmd.manufactured_date,
        expiry_date=cmd.expiry_date,
    )


async def update_batch(cmd: AddBatch) -> model.Batch:
    return model.batch_factory(
        id_=cmd.id_,
        sku_id=cmd.sku_id,
        purchase_order=cmd.purchase_order,
        material_handle=cmd.material_handle,
        manufactured_date=cmd.manufactured_date,
        expiry_date=cmd.expiry_date,
    ).update()


async def add_product(cmd: AddBatch) -> model.Product:
    return model.product_factory(
        id_=cmd.id_,
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
        id_=cmd.id_,
        name=cmd.name,
        sub_category=cmd.sub_category,
    )


# import command
# from source.domain.model import Shipment, Order, OrderDetail,
# from source.domain import model

# async def add_shipment(cmd:command.AddShipment)

# async def add_batch(cmd: command.AddBatch) -> model.Batch:
#     return model.batch_factory()  # pass factory argu
