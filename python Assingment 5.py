assingment 1 and 2




Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = 100  # Default battery level

    def call(self, number):
        print(f"{self.model} is calling {number}...")

    def charge(self):
        self.battery = 100
        print(f"{self.model} is now fully charged!")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB) - Battery: {self.battery}%"

# Subclass (Inheritance)
class iPhone(Smartphone):
    def __init__(self, model, storage, ios_version):
        super().__init__("Apple", model, storage)
        self.ios_version = ios_version

    def update_ios(self):
        print(f"Updating {self.model} to iOS {self.ios_version}...")

    # Polymorphism example (overriding)
    def call(self, number):
        print(f"{self.model} (FaceTime) is calling {number}...")

# --- Example Usage ---
phone1 = Smartphone("Samsung", "Galaxy S24", 256)
phone2 = iPhone("iPhone 15", 512, "17.0")

print(phone1)
phone1.call("123-456-7890")
phone1.charge()

print(phone2)
phone2.call("987-654-3210")
phone2.update_ios()
🎭 Activity 2: Polymorphism Challenge (move() method)
python
Copy code
class Car:
    def move(self):
        print("Driving on the road 🚗")

class Plane:
    def move(self):
        print("Flying in the sky ✈️")

class Boat:
    def move(self):
        print("Sailing on the water 🚢")

# --- Example Usage ---
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()









Ask ChatGPT
