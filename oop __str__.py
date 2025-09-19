
class parson:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"her name is {self.name} and she is {self.age} years old"


pi=parson("alif",22)
print(pi)
