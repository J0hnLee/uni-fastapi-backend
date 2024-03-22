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

# This should be different database
redis = get_redis_connection(
    host=redis_host,
    port=redis_api_port,
    password=secret_key,
    decode_responses=True
)


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str  # pending, complete, refunded

    class Meta:
        database = redis
