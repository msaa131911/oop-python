#oop 2
#just a pattis 
class student:
    name=""
    roll=""
    gpa=""

    def __init__(self,name,roll,gpa):
        self.name=name
        self.roll=roll
        self.gpa=gpa


    def display(self):
        print(self.name,self.roll,self.gpa)
try:
    rahim=student("rahim",21,1)
    rahim.display()

    sakib=student("sakib",22,2)
    sakib.display()
except Exception as e:
    print(e)
finally:
    print("finally block")
