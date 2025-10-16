class Student:
    def __init__(self,Id,name):
        self.studentID=Id
        self.Name=name
    def display(self):
        print("Student id: ",self.studentID)
        print("Student Name: ",self.Name)
class Marks(Student):
    def __init__(self,Id,name,algo,ds,calc):
        super().__init__(Id,name)
        self.marks_algo=algo
        self.marks_ds=ds
        self.marks_calc=calc
    def display(self):
        super().display()
        print("Algo marks: ",self.marks_algo)
        print("data structures marks: ",self.marks_ds)
        print("calculus marks: ",self.marks_calc)
class result(Marks):
    def __init__(self,Id,name,algo,ds,calc):
        super().__init__(Id,name,algo,ds,calc)
    def display(self):
        super().display()
        print("total marks: ",self.marks_algo+self.marks_ds+self.marks_calc)
        print("average marks: ",(self.marks_algo+self.marks_ds+self.marks_calc)/3)

res1=result(12,"Aisha",23,45,34)
res1.display()
