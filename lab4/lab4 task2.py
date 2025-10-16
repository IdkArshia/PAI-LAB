from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class square(Shape):
    def area(self,length):
        self.area=length*length
        return self.area
class rectangle(Shape):
    def area(self,length,wid):
        self.area=length*wid
        return self.area    
class triangle(Shape):
    def area(self,base,height):
        self.area=0.5*base*height
        return self.area 
s1=square()
r1=rectangle()
t1=triangle()
print("Area of square: ",s1.area(5))
print("Area of rectangle: ",r1.area(4,5))
print("Area of triangle: ",t1.area(3,5))