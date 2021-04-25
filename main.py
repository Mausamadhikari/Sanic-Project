from sanic import Sanic
from sanic.response import json

app = Sanic(_name_)


@app.route('/')
async def test(request):
    return json({'hello': 'world welcome to sanic framework api fastest web development'})


@app.route('/about')
async def test(request):
    return json({'hello': 'mausam'})


@app.get('/batch')
async def get_batch(request):
    pass


@app.get('/batch/<int:id>')
async def get_batch_product(request):
    pass


@app.get('/sku')
async def get_sku(request):
    pass


@app.get('/ordeline')
async def get_orderline(request):
    pass

if _name_ == '_main_':
    app.run(debug=True)
