products = [
    {"name": "Laptop", "price": 15000000},
    {"name": "Mouse", "price": 200000},
    {"name": "Keyboard", "price": 500000}
]

product_name = input("nhap san pham: ").strip()
found_product = None
for product in products:
    if product["name"].lower() == product_name.lower():
        found_product = product
        break

if found_product:
    print("san pham:", found_product["name"], ", price:", found_product["price"])
else:
    print("khong tim thay")