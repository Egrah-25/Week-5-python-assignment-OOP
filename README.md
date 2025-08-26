# Week-5-python-assignment-OOP
This project demonstrates Object-Oriented Programming (OOP) concepts in Python, including classes, attributes, methods, constructors, inheritance, encapsulation, and polymorphism.

📌 Assignment 1: Design Your Own Class!
Example: Smartphone Class 📱
# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Child Class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery

# Creating objects
phone1 = Smartphone("Samsung", "S24 Ultra", "256GB", "5000mAh")
phone2 = Smartphone("Apple", "iPhone 15", "512GB", "4200mAh")

# Using methods
print(phone1.device_info())  # Samsung S24 Ultra
print(phone2.call("Alice"))  # Calling Alice...
print(phone1.charge())       # S24 Ultra is charging 🔋

✅ Concepts used:

Class & Objects (Smartphone, Device)
Constructor (__init__)
Inheritance (Smartphone inherits from Device)
Encapsulation (attributes bundled inside class)

📌 Activity 2: Polymorphism Challenge 🎭

We’ll model different vehicles with the same method move() but different behaviors.

class Car:
    def move(self):
        return "🚗 Driving on the road"

class Plane:
    def move(self):
        return "✈️ Flying in the sky"

class Boat:
    def move(self):
        return "⛵ Sailing on water"

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())

Output:

🚗 Driving on the road  
✈️ Flying in the sky  
⛵ Sailing on water

✅ Concepts used:

Polymorphism (same method move() behaves differently)
Looping through objects with shared behavior

🚀 How to Run

1. Save the code in a file, e.g., oop_assignment.py
2. Run in terminal:
python oop_assignment.py

🧠 What I Learned

Designing custom Python classes
Using constructors for unique objects
Applying inheritance to extend functionality
Implementing polymorphism for flexible methods
