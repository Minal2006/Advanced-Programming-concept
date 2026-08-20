products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15
}

while True:
    print("\n1. Add Product")
    print("2. Update Quantity")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Display Quantity Below 10")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter product: ")
        quantity = int(input("Enter quantity: "))
        products[name] = quantity

    elif choice == 2:
        name = input("Enter product: ")
        if name in products:
            quantity = int(input("Enter new quantity: "))
            products[name] = quantity
        else:
            print("Product not found")

    elif choice == 3:
        name = input("Enter product: ")
        if name in products:
            del products[name]
        else:
            print("Product not found")

    elif choice == 4:
        name = input("Enter product: ")
        if name in products:
            print("Quantity:", products[name])
        else:
            print("Product not found")

    elif choice == 5:
        for name, quantity in products.items():
            if quantity < 10:
                print(name, ":", quantity)

    elif choice == 6:
        break

    else:
        print("Invalid choice")