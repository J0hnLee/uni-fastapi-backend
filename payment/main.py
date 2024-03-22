from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from typing import Union
from starlette.requests import Request
import requests
from model import Order
import time
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/orders/{pk}")
def get(pk: str):
    return Order.get(pk)


@app.post("/orders")
async def create(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()
    # print(body)
    req = requests.get("http://localhost:8000/products/%s" % body['id'])
    product = req.json()
    order = Order(
        product_id=body["id"],
        price=product["price"],
        fee=0.2*product["price"],
        total=1.2*product["price"],
        quantity=body["quantity"],
        status='pending'

    )
    order.save()
    background_tasks.add_task(order_completed, order)
    # order_completed(order)
    return order


def order_completed(order: Order):
    # pretend order to be complete need 5 sec.
    time.sleep(10)
    order.status = "Completed"
    order.save()
