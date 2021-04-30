from src.models import Batch
def test_update_batch_model():
    batch1 = Batch(
        "id_": uuid.uuid4().hex,
        "sku_id": uuid.uuid4().hex,
        "purchase_order": 101,
        "material_handle": 3,
        "manufactured_date": "2024-01-01T00:00",
        "expiry_date": "2001-01-01T00:00",
    )

    batch2 = Batch(
        id_ =uuid.uuid4().hex,
        sku_id= uuid.uuid4().hex,
        purchase_order= 201,
        material_handle= 5,
        manufactured_date= "2022-01-01T00:00",
        expiry_date= "2005-01-01T00:00",
    )