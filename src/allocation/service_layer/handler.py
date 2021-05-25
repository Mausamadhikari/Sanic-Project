from src.allocation.domain import model
from src.allocation.domain.command import (
    CreateBatch,
    BatchCommand,
    CreateCategory,
    CreateProduct,
    ProductCommand,
    UpdadteBatchPurchaseQuantity,
    UpdadteBatchQuantity,
    UpdateProduct,
)


async def add_batch(cmd: CreateBatch) -> model.Batch:
    return model.batch_factory(
        sku_id=cmd.sku_id,
        purchase_quantity=cmd.purchase_quantity,
        quantity=cmd.quantity,
        material_handle=cmd.material_handle,
        manufactured_date=cmd.manufactured_date,
        expiry_date=cmd.expiry_date,
    )


async def update_batch(cmd: BatchCommand) -> model.Batch:
    if isinstance(cmd, UpdadteBatchQuantity):
        return cmd.batch.update({"quantity": cmd.quantity})
    if isinstance(cmd, UpdadteBatchPurchaseQuantity):
        return cmd.batch.update({"purchase_order": cmd.purchase_order})


async def add_product(cmd: CreateProduct) -> model.Product:
    return model.product_factory(
        category=cmd.category,
        name=cmd.name,
        description=cmd.description,
        slug=cmd.slug,
        brand=cmd.brand,
        status=cmd.status,
        updated_date=cmd.updated_date,
    )


async def update_product(cmd: ProductCommand) -> model.Product:
    # if isinstance(cmd, UpdateProductCategory):
    #     return cmd.product.update({"category": cmd.category})
    # if isinstance(cmd, UpdateProductName):
    #     return cmd.product.update({"name": cmd.name})
    # if isinstance(cmd, UpdateProductDescription):
    #     return cmd.product.update({"description": cmd.description})
    # if isinstance(cmd, UpdateProductSlug):
    #     return cmd.product.update({"slug": cmd.slug})
    # if isinstance(cmd, UpdateProductBrand):
    #     return cmd.product.update({"brand": cmd.brand})
    # if isinstance(cmd, UpdateProductStatus):
    #     return cmd.product.update({"status": cmd.status})
    # if isinstance(cmd, UpdateProductUpdatedDate):
    #     return cmd.product.update({"updated_date": cmd.updated_date})
    if isinstance(cmd, UpdateProduct):
        return cmd.product.update(
            {
                "category": cmd.category,
                "name": cmd.name,
                "description": cmd.description,
                "slug": cmd.slug,
                "brand": cmd.brand,
                "status": cmd.status,
                "updated_date": cmd.updated_date,
            }
        )


async def add_category(cmd: CreateCategory) -> model.Category:
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
