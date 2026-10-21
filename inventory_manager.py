# Topic: Mini project - inventory with dict
stock = {"rice": 10, "oil": 5}
stock["sugar"] = 8  # add item
stock["rice"] -= 3  # sell 3 rice
for item, qty in stock.items():
    print(f"{item:<6} {qty}")
print("Total items:", sum(stock.values()))
