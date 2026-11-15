from shop import Product, find_by_name

products = [Product("A1", "Mouse", 1000), Product("B2", "Keyboard", 2500)]

def test_find_existing():
    assert [p.sku for p in find_by_name(products, "mou")] == ["A1"]

def test_find_missing():
    assert find_by_name(products, "Monitor") == []
new test line
