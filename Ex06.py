inventory = [
    {"id": 1, "name": "Laptop", "quantity": 5},
    {"id": 2, "name": "Mouse", "quantity": 20},
    {"id": 3, "name": "Keyboard", "quantity": 10}
]

new_product = {"id": 4, "name": "Monitor", "quantity": 3}
inventory.append(new_product)
print("Da them sp moi")

update_id = 2
new_quantity = 25
for product in inventory:
    if product["id"] == update_id:
        product["quantity"] = new_quantity
        print("Da cap nhat so luong sp id", update_id)
        break
else:
    print("khong tim thay sp")

delete_id = 1
for i in range(len(inventory)):
    if inventory[i] ["id"] == delete_id:
        del inventory[i]
        print("deleted", delete_id)
        break
else:
    print("khong tim thay sp can delete")

print("danh sach kho hang sau update:")
for product in inventory:
    print(product)