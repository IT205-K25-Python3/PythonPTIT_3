product = {
    "name":"laptop",
    "price":15000000,
    "quantity":5
}

while True:
    choice = input("""
1. in ten san pham
2. cap nhat gia thanh 14 trieu
3. them brand = dell
4. xoa key quantity
0. thoat
chon: """)

    match choice:
        case "1":
            print("ten san pham:", product)
        case "2":
            product["price"] = 14000000
            print("da cap nhat:", product)
        case "3":
            product["brand"] = "dell"
            print("da them:", product)
        case "4":
            del product["quantity"]
            print("da xoa:", product)
        case "0":
            print("thoat chuong trinh.")
            break
        case _:
            print("lua chon khong hop le")