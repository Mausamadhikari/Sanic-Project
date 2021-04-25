from sanic import Sanic
from sanic.response import text, json
from src.models import ProductModel, BatchModel, CategoryModel
from datetime import datetime, date

app = Sanic(__name__)


data_product_list = [{
    'id': 2000,
    'category': 424,
    'name': 'HP inspiron 5000',
    'description': 'This is i5 11th generation intel core Laptop with 8GB RAM',
    'slug': 'https://guthib.com/mausamadhikari',
    'brand': 'HP',
    'status': True,
    'updated_date': "2005-01-01T00:00"
}, {
    'id': 1000,
    'category': 212,
    'name': 'Dell inspiron 5000',
    'description': 'This is i5 10th generation intel core Laptop with 8GB RAM',
    'slug': 'https://guthib.com/',
    'brand': 'Dell',
    'status': True,
    'updated_date': "2001-01-01T00:00"
}]

data_batch_list = [{
    'id': 1000,
    'sku_id': 100,
    'purchase_order': 101,
    'material_handle': 3,
    'manufactured_date': "2024-01-01T00:00",
    'expiry_date': "2001-01-01T00:00"
}, {
    'id': 2000,
    'sku_id': 200,
    'purchase_order': 201,
    'material_handle': 5,
    'manufactured_date': "2022-01-01T00:00",
    'expiry_date': "2005-01-01T00:00"
}]

data_category = dict(
    id=1000,
    name="Electronics",
    sub_category=1001
)


def default(o):
    """
    Format according to ISO 8601 	Value ranges
    Year (Y) 	                    YYYY, four-digit, abbreviated to two-digit
    Month (M) 	                    MM, 01 to 12
    Week (W) 	                    WW, 01 to 53
    Day (D) 	                    D, day of the week, 1 to 7
    Hour (h) 	                    hh, 00 to 23, 24:00:00 as the end time
    Minute (m) 	                    mm, 00 to 59
    Second (s) 	                    ss, 00 to 59
    Decimal fraction (f) 	        Fractions of seconds, any degree of accuracy 


    date.isoformat()->str
    Return a string representing the date in ISO 8601 format, YYYY-MM-DD
    """
    if isinstance(o, (date, datetime)):
        return o.isoformat()


@app.get("/")
async def hello_world(request):
    return text("Hello, world. 123")


@app.get("/batch")
async def get_batches(request):
    new_batch = list()
    for i in range(len(data_batch_list)):
        try:
            batch_with_id = data_batch_list[i]
            batch = BatchModel(**batch_with_id)
            batch.manufactured_date = default(batch.manufactured_date)
            batch.expiry_date = default(batch.expiry_date)
            new_batch.append(batch.dict())
            print(new_batch)
        except Exception as e:
            return json(e)
    return json(new_batch)


@app.get("/batch/<id:int>")
async def get_batches_by_id(request, id: int):
    for i in range(len(data_batch_list)+1):
        try:
            if data_batch_list[i]['id'] == id:
                batch_with_id = data_batch_list[i]
                batch = BatchModel(**batch_with_id)
                batch.manufactured_date = default(batch.manufactured_date)
                batch.expiry_date = default(batch.expiry_date)
                return json(batch.dict())
        except Exception as e:
            return json(e)


@app.get("/category")
async def get_category(request):
    category = CategoryModel(**data_category)
    return json(category.dict())

app.add_route(get_category, '/categories')


@app.route("/product", methods=['POST', 'GET'])
async def get_product(request):
    # data_product["manufactured_date"] = myconverter(
    #     data_product["manufactured_date"])
    # data_product["updated_date"] = myconverter(
    #     data_product["updated_date"])
    # m = ProductModel(**data_product)

    # m.manufactured_date = default(m.manufactured_date)
    # m.updated_date = default(m.updated_date)
    # return json(m.dict())
    new_product = list()
    for i in range(len(data_product_list)):
        try:
            product_with_id = data_product_list[i]
            product = ProductModel(**product_with_id)
            product.updated_date = default(product.updated_date)
            new_product.append(product.dict())
            print(new_product)
        except Exception as e:
            return json(e)
    return json(new_product)


# @app.route("/product", methods=['POST'])
# async def get_product(request):
#     request.form
#     new_product = list()
#     return json(new_product)


@app.route('/product/<id:int>')
async def get_product_by_id(request, id: int):
    for i in range(len(data_product_list)+1):
        try:
            if data_product_list[i]['id'] == id:
                product_with_id = data_product_list[i]
                product = ProductModel(**product_with_id)
                product.updated_date = default(product.updated_date)
                return json(product.dict())

        except Exception as e:
            return json(e)


if __name__ == "__main__":
    app.run(debug=True)
