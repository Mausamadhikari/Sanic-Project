from src.models import ProductModel
from pydantic import ValidationError

data_product = dict(
    id=1000,
    category=212,
    batch=2,
    name='Dell inspiron 5000',
    price=85000,
    description='This is i5 10th generation intel core Laptop with 8GB RAM',
    slug='https://guthib.com/',
    brand='Dell',
    status=True,
    manufactured_date="2022-01-01T00:00",
    updated_date="2001-01-01T00:00"
)

try:
    m = ProductModel(**data_product)
    print(m.dict())
except ValidationError as e:
    print(e)
