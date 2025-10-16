class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def calc_bonus(self):
        pass
class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calc_bonus(self):
        return self.salary*1.2
    def hire(self):
        print("The manager is hiring")
class Developer(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calc_bonus(self):
        return self.salary*1.1
    def WriteCode(self):
        print("developer is writing code")
class SeniorManager(Manager):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calc_bonus(self):
        return self.salary*1.3
d1=Developer("Ahmed",52000)
print("Bonus: ",d1.calc_bonus())
d1.WriteCode()
m1=Manager("Arshia",520000)
print("Bonus: ",d1.calc_bonus())
m1.hire()
sm1=SeniorManager("Laiba",600000)
print("Bonus: ",sm1.calc_bonus())


    

