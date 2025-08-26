# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Inherited Class
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)   # call parent constructor
        self.os = os
        self.storage = storage

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}")

    def take_photo(self):
        print(f"📸 Taking a photo with {self.device_info()}")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", "Android", "256GB")
phone2 = Smartphone("Apple", "iPhone 15", "iOS", "128GB")

phone1.make_call("+254742651608")
phone2.take_photo()
