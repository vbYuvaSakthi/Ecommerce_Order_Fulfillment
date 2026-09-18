import pandas as pd
customers = pd.read_csv(
    "output/customers.csv"
)
orders = pd.read_csv(
    "output/orders.csv"
)
order_items = pd.read_csv(
    "output/order_items.csv"
)
assert customers.shape[0] > 0
print("PASS : Customer Data Loaded")

assert orders.shape[0] > 0
print("PASS : Orders Data Loaded")

assert order_items["Quantity"].min() > 0
print("PASS : No Negative Quantity")

assert order_items["Net Price"].min() > 0
print("PASS : No Negative Price")

print("\nALL TESTS PASSED")
