from __future__ import annotations
from src.allocation.domain import model
from src.allocation.domain.model import Batch, OrderLine, Product
from src.allocation.service_layer import unit_of_work
from src.allocation.adapters.repository import BatchRepository
from src.allocation.adapters.repository import CategoryRepository
from src.allocation.adapters.repository import ProductRepository
from src.allocation.service_layer import abstract, handler
from src.allocation.domain import command


class InvalidSku(Exception):
    pass


async def add_batch(
    validated_data: abstract.AddBatch, uow: unit_of_work.BatchUnitOfWork
) -> None:
    # call commmand.py
    with uow:
        batch = await handler.add_batch(
            command.CreateBatch(
                sku_id=validated_data.sku_id,
                purchase_quantity=validated_data.purchase_quantity,
                quantity=validated_data.quantity,
                material_handle=validated_data.material_handle,
                manufactured_date=validated_data.manufactured_date,
                expiry_date=validated_data.expiry_date,
            )
        )  #
        repo = BatchRepository()
        repo.add(batch)
        uow.commit()


async def allocate(
    cmd: command.Allocate,
    uow: unit_of_work.BatchUnitOfWork,
):
    line = OrderLine(sku_id=cmd.sku_id, qty=cmd.qty)
    with uow:
        batch = uow.batchref.get(sku=line.sku_id)
        if batch is None:
            raise InvalidSku(f"Invalid sku {line.sku_id}")
        await model.allocate(batch, line)
        uow.commit()
        return batch


# def reallocate(
#     event: events.Deallocated,
#     uow: unit_of_work.AbstractUnitOfWork,
# ):
#     allocate(commands.Allocate(**asdict(event)), uow=uow)


async def update_batch_quantity(
    id_: int,
    validated_data: abstract.UpdateQuantity,
    uow: unit_of_work.BatchUnitOfWork,
) -> None:
    with uow() as u:
        repo = BatchRepository()
        batch = repo.get(id_)  # why not batch.quantity = validated_data.quantity
        batch = handler.update_batch(
            command.UpdadteBatchQuantity(batch=batch, quantity=validated_data)
        )
        await repo.update(batch)
        u.commit()


async def add_product(
    validated_data: abstract.AddProduct, uow: unit_of_work.ProductUnitOfWork
) -> Product:
    with uow():
        product = handler.add_product(
            command.CreateProduct(
                category=validated_data.category,
                name=validated_data.name,
                description=validated_data.description,
                slug=validated_data.slug,
                brand=validated_data.brand,
                status=validated_data.status,
                updated_date=validated_data.updated_date,
            )
        )
        repo = ProductRepository()
        repo.add(product)
        uow.commit()
        return product


async def update_product(
    id_: int,
    validated_data: abstract.UpdateProduct,
    uow: unit_of_work.ProductUnitOfWork,
) -> None:
    with uow() as u:
        repo = ProductRepository()
        product = repo.get(id_)
        print(validated_data)
        product_ = handler.update_product(
            command.UpdateProduct(
                product=product,
                category=validated_data.category
                if validated_data.category
                else product.category,
                name=validated_data.name if validated_data.name else product.name,
                description=validated_data.description
                if validated_data.description
                else product.description,
                slug=validated_data.slug if validated_data.slug else product.slug,
                brand=validated_data.brand if validated_data.brand else product.brand,
                status=validated_data.status
                if validated_data.status
                else product.status,
                updated_date=validated_data.updated_date
                if validated_data.updated_date
                else product.updated_date,
            )
        )
        print("just before updating values of product_", product_)
        repo.update(id_, product_)
        # event trigger garne yaha
        u.commit()
    print("Data After Updated", repo.get(id_))


async def add_category(validated_data: abstract.AddCategory) -> None:
    category = handler.add_category(
        command.AddCategory(
            name=validated_data.name,
            sub_category=validated_data.sub_category,
        )
    )
    repo = CategoryRepository()
    await repo.add_category(category)
