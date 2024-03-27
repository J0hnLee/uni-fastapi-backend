from model import redis, Product
import time
key = "order_completed"
group = "inventory-group"

try:
    redis.xgroup_create(key, group)

except:
    print("Group already exist.")

while True:
    print("consumer starting.")
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)
        # {key: '>'} 是一個字典，用於指定要讀取的消息 ID。
        # 在這裡，'>' 表示從目前位置之後的消息開始讀取，
        # 也就是從最新的消息開始讀取。
        if results != []:
            for result in results:
                obj = result[1][0][1]
                product = Product.get(obj["product_id"])
                if product:

                    product.quantity = product.quantity-int(obj['quantity'])
                    product.save()
                else:
                    redis.xadd('refund_order', obj, "*")

        # print(results)
    except Exception as e:
        print(str(e))
    time.sleep(1)
