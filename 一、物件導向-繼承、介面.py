#一、物件導向-繼承、介面
#今有車輛「汽車」和「機車」,請使用物件的繼承/介面描述二者相同與差異,及二物件的執行程式碼

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def start(self):
        print(f"The {self.color} car with brand {self.brand} starts.")

    def stop(self):
        print(f"The {self.color} car with brand {self.brand} stops.")

class Motorcycle(Vehicle):
    def start(self):
        print(f"The {self.color} motorcycle with brand {self.brand} starts.")

    def stop(self):
        print(f"The {self.color} motorcycle with brand {self.brand} stops.")

car = Car("Toyota", "red")
car.start()
car.stop()

motorcycle = Motorcycle("Honda", "blue")
motorcycle.start()
motorcycle.stop()
