cart = [
    {"name": "Sách", "price": 50000, "quantity": 2},
    {"name": "Bút", "price": 5000, "quantity": 10},
    {"name": "Vở", "price": 12000, "quantity": 5}
]

print("tien tung san pham:")
for item in cart:
    total_item = item["price"] * item["quantity"]
    print(item["name"], ":", total_item, "VND")

total_cart = sum(item["price"] * item["quantity"] for item in cart)
print("tong toan bo gio hang:", total_cart, "VND")