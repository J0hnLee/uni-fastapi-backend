from fastapi import FastAPI
from typing import Union
from redis_om import get_redis_connection
# import sys
# print(sys.path)

from dotenv import load_dotenv
import os
# 加载 .env 文件中的环境变量
load_dotenv()

# 使用环境变量
redis_host = os.getenv("REDIS_PUBLIC_ENDPOINT")
redis_api_port = os.getenv("REDIS_PUBLIC_ENDPOINT_PORT")
secret_key = os.getenv("REDIS_PUBLIC_ENDPOINT_SECURITY_KEY")

# 在这里使用您的环境变量

app = FastAPI()
redis = get_redis_connection(
    host=redis_host,
    port=redis_api_port,
    password=secret_key,
    decode_responses=True
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
