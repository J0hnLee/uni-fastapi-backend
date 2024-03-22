from model import Product


def format(pk: str):
    product = Product.get(pk)
    print(product)
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }
