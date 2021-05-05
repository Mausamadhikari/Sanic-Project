from __future__ import annotations
from src.allocation.adapters.repository import BatchRepository, Categoryrepository, Productrepository
from src.allocation.service_layer import abstract, handler
from src.allocation.domain import command


def add_batch(validated_data: abstract.AddBatch) -> None:  # call commmand.py
    batch = handler.add_batch(
        command.AddBatch(
            id_=validated_data.id_,
            sku_id=validated_data.sku_id,
            purchase_order=validated_data.purchase_order,
            material_handle=validated_data.material_handle,
            manufactured_date=validated_data.manufactured_date,
            expiry_date=validated_data.expiry_date,
        )
    )  #
    repo = BatchRepository
    repo.add_batch(batch)


def update_batch(validated_data: command.AddBatch) -> None:
    batch = handler.update_batch(
        command.AddBatch(
            id_=validated_data.id_,
            sku_id=validated_data.sku_id,
            purchase_order=validated_data.purchase_order,
            material_handle=validated_data.material_handle,
            manufactured_date=validated_data.manufactured_date,
            expiry_date=validated_data.expiry_date,
        )
    )
    repo = BatchRepository
    repo.update_batch(batch)


def add_product(validated_data: command.AddProduct) -> None:
    product = handler.add_product()(
        command.AddProduct(
            id_=validated_data.id_,
            category=validated_data.category,
            name=validated_data.name,
            description=validated_data.description,
            slug=validated_data.slug,
            brand=validated_data.brand,
            status=validated_data.status,
            updated_date=validated_data.updated_date,
        )
    )
    repo = Productrepository
    repo.add_product(product)


def add_category(validated_data: command.AddCategory) -> None:
    category = handler.add_category(
        command.AddCategory(
            id_=validated_data.id_,
            name=validated_data.name,
            sub_category=validated_data.sub_category,
        )
    )
    repo = Categoryrepository
    repo.add_category(category)
