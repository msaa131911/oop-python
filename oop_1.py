class student():
    name=""
    age=""
    roll=""

    def Valueset(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
    
    def display(self):
        print(self.name,self.age,self.roll)

rahim=student()
rahim.Valueset("rahim",21,1)
rahim.display()

sakib=student()
sakib.Valueset("sakib",22,2)
sakib.display()
