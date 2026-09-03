from products.product_details import product_details
from products.product_price import product_price

from customers.customer_details import customer_details
from customers.customer_address import customer_address

from orders.order_details import order_details
from orders.order_status import order_status

from payments.payment_details import payment_details
from payments.payment_status import payment_status


print("========== E-COMMERCE APPLICATION ==========")

# Product information
product_id, product_name = product_details()
price, quantity, total = product_price()

print("\n----- PRODUCT INFORMATION -----")
print("Product ID :", product_id)
print("Product    :", product_name)
print("Price      :", price)
print("Quantity   :", quantity)
print("Total      :", total)


# Customer information
customer_id, customer_name = customer_details()
city, state = customer_address()

print("\n----- CUSTOMER INFORMATION -----")
print("Customer ID :", customer_id)
print("Name        :", customer_name)
print("City        :", city)
print("State       :", state)


# Order information
order_id, product, order_quantity = order_details()

print("\n----- ORDER INFORMATION -----")
print("Order ID    :", order_id)
print("Product     :", product)
print("Quantity    :", order_quantity)
print("Status      :", order_status())


# Payment information
payment_id, amount = payment_details()

print("\n----- PAYMENT INFORMATION -----")
print("Payment ID  :", payment_id)
print("Amount      :", amount)
print("Status      :", payment_status())