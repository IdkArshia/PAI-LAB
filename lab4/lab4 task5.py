class Vehicles:
    def __init__(self,make,model,rp):
        self.make=make
        self.model=model
        self.rp=rp
        self.availability=True 
    def check(self):
        if(self.availability):
            return True
        else:
            return False
    def calc_rent(self,days):
        return self.rp*days
    def display(self):
        print("Make: ",make)
        print("Model: ",model)
        print("rental price: ",rp)
class car(Vehicles):
    def __init__(self,make,model,rp):
        super().__init__(make,model,rp)

class SUV(Vehicles):
    def __init__(self,make,model,rp):
        super().__init__(make,model,rp)

class Truck(Vehicles):
    def __init__(self,make,model,rp):
        super().__init__(make,model,rp)

class RentalReservation:
    def __init__(self,sd,ed,vehicle,cust,days):
        self.sd=sd
        self.ed=ed
        self.price=vehicle.calc_rent(days)
        vehicle.availability=False
        cust.hist(self)

class Customer:
    rentHist=[]
    def __init__(self,name,ci):
        self.name=name
        self.ci=ci
    def hist(self,Rr):
        self.rentHist.append(Rr)

T1=Truck("abc",2024,3450)
c1=Customer("Ahmed",321232345)
r1=RentalReservation(1,18,T1,c1,17)
print(c1.rentHist[0].price)
car1=car("xyz",2024,3400)
r1=RentalReservation(1,18,car1,c1,17)
print(c1.rentHist[1].price)