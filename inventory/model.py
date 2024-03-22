from redis_om import get_redis_connection, HashModel

import redis

from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

# 使用环境变量
redis_host = os.getenv("REDIS_PUBLIC_ENDPOINT")
redis_api_port = os.getenv("REDIS_PUBLIC_ENDPOINT_PORT")
secret_key = os.getenv("REDIS_PUBLIC_ENDPOINT_SECURITY_KEY")

redis = get_redis_connection(
    host=redis_host,
    port=redis_api_port,
    password=secret_key,
    decode_responses=True
)


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis
