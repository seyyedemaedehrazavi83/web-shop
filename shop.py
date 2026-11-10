class Product:
    def __init__(self, sku, name, price):
        if not sku:
            raise ValueError("sku iss required")
        self.sku = sku
        self.name = name
        self.price = price

def find_by_name(products, text):
    return [p for p in products if text.lower() in p.name.lower()]


def apply_discount(price , percen):
    return price * (100 - percen) / 100


def add_tax(price , rate=0.2):
    return price * (1 + rate)