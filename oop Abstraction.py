#oop Abstraction

from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self,dmn1,dmn2):
        self.dmn1=dmn1
        self.dmn2=dmn2
    
    @abstractmethod
    def area(self):
        pass
    
class tringle(shape):
    def area(self):
        area=0.5*self.dmn1*self.dmn2
        print(area)

class rectangle(shape):
    def area(self):
        area=self.dmn1*self.dmn2
        print(area)


t1=tringle(10,20)
t1.area()

r1=rectangle(10,20)
r1.area()