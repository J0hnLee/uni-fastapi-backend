from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from model import Product
from utils import format


# 在这里使用您的环境变量

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/products")
def all():
    # format(Product.all_pks())
    return [format(pk) for pk in Product.all_pks()]


# HashModel is not supported by the latest version of Pydantic.

@app.post('/products')
def create(product: Product):
    return product.save()


@app.get('/products/{pk}')
def get(pk: str):
    return Product.get(pk)


@app.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)
