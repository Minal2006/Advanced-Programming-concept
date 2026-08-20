cities = {
    "Satara": 7000000,
    "Kolhapur": 20000000,
    "Pune": 19000000,
    "Mumbai": 1500000
}
city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print(cities)
else:
    print("City not found")