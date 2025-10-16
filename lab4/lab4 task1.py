class Vehicle:
    fare=0
    def __init__(self, capacity):
        self.capacity=capacity
    
    def calcfare(self):
        self.fare=self.capacity*100
        return self.fare
class Bus(Vehicle):
    def __init__(self,capacity):
        super().__init__(capacity)
    def calcfare(self):
        super().calcfare()
        self.fare=self.fare*1.1
        return self.fare
bus1=Bus(20)
print(bus1.calcfare())
