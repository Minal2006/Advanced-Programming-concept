from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 0

class HomeDeliveryOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 50

r = RestaurantOrder()
h = HomeDeliveryOrder()

print("Restaurant Bill:", r.calculate_bill() + r.delivery_charge())
print("Home Delivery Bill:", h.calculate_bill() + h.delivery_charge())