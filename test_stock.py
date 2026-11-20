# test_stock.py
from shop import in_stock

stock = {"P001": 3 , "P002": 0}

assert in_stock(stock , "P001")
assert not in_stock(stock , "P002")

print("Stock test passed")
