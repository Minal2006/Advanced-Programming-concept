
cart = []


cart.append("Apple")
cart.append("Milk")
cart.append("Bread")
print("Shopping Cart:", cart)


cart.remove("Milk")
print("After Removing Milk:", cart)


item = "Apple"
if item in cart:
    print(item, "is found in the cart.")
else:
    print(item, "is not found in the cart.")


print("Total Items:", len(cart))