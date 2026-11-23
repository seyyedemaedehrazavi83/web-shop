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
    percen = min(percen , 100)
    return price * (100 - percen) / 100



def add_tax(price , rate=0.15):
    return price * (1 + rate)

def apply_coupon(price):
    return max(price - 5, 0)

def test_find_case_insensitive():
    assert [p.sku for p in find_by_name(products , "KEY")] == ["B2"]

def format_price(price):
return f"{price:,} Toman"


def list_name(products):
return [p.name for p in products]
