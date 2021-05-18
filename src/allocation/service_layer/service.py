from __future__ import annotations
from src.allocation.domain import model
from src.allocation.domain.model import Batch
from src.allocation.service_layer import unit_of_work
from src.allocation.adapters.repository import BatchRepository
from src.allocation.adapters.repository import CategoryRepository
from src.allocation.adapters.repository import ProductRepository
from src.allocation.service_layer import abstract, handler
from src.allocation.domain import command


async def add_batch(
    validated_data: abstract.AddBatch, uow: unit_of_work.BatchUonitOfWork
) -> None:
    # call commmand.py
    with uow:
        batch = handler.add_batch(
            command.CreateBatch(
                sku_id=validated_data.sku_id,
                purchase_order=validated_data.purchase_order,
                quantity=validated_data.quantity,
                material_handle=validated_data.material_handle,
                manufactured_date=validated_data.manufactured_date,
                expiry_date=validated_data.expiry_date,
            )
        )  #
        repo = BatchRepository()
        await repo.add(batch)
        uow.commit()


async def update_batch_quantity(
    id_: int,
    validated_data: abstract.UpdateQuantity,
    uow: unit_of_work.BatchUnitOfWork,
) -> None:
    with uow:
        repo = BatchRepository()
        batch = repo.get(id_)  # why not batch.quantity = validated_data.quantity
        batch = handler.update_batch(
            command.UpdadteBatchQuantity(batch=batch, quantity=validated_data.quatity)
        )
        await repo.update(batch)
        uow.commit()


async def add_product(
    validated_data: abstract.AddProduct, uow: unit_of_work.ProductUnitOfWork
) -> None:
    with uow:
        product = handler.add_product(
            command.AddProduct(
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
        await repo.add(product)
        uow.commit()


async def update_product_category(
    id_: int,
    validated_data: abstract.UpdateProductCategory,
    uow: unit_of_work.ProductUnitOfWork,
) -> None:
    with uow:
        repo = ProductRepository()
        product = repo.get(id_)
        product_ = handler.update_product(
            command.UpdateProduct(product=product, category=validated_data.category)
        )
        await repo.update(id_, product_)
        #event trigger garne yaha
        uow.commit()


async def add_category(validated_data: abstract.AddCategory) -> None:
    category = handler.add_category(
        command.AddCategory(
            name=validated_data.name,
            sub_category=validated_data.sub_category,
        )
    )
    repo = CategoryRepository()
    await repo.add_category(category)
