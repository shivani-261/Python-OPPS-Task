from abc import ABC,abstractmethod 
    
class Car(ABC):
    @abstractmethod
    def features(self, max_speed, fuel, seat):
        pass

class BMW(Car):
    def show(self):
        print("I am BMW")

    def features(self, max_speed, fuel, seat):
        print("Max Speed:", max_speed)
        print("Fuel Type:", fuel)
        print("Number of Seats:", seat)

class Suzuki(Car):
    def show(self):
        print("I am Suzuki")

    def features(self, max_speed, fuel, seat):
        print("Max Speed:", max_speed)
        print("Fuel Type:", fuel)
        print("Number of Seats:", seat)

class Mahindra(Car):
    def show(self):
        print("I am Mahindra")

    def features(self, max_speed, fuel, seat):
        print("Max Speed:", max_speed)
        print("Fuel Type:", fuel)
        print("Number of Seats:", seat)


b1 = BMW()
b1.show()
b1.features(250, "Petrol", 5)

s1=Suzuki()
s1.show()
s1.features(220,"petrol",4)

m1=Mahindra()
m1.show()
m1.features(180,"Diesel",5)


