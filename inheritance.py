class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"The name of {self.id} is {self.name}")

class programmer(Employee):
    def showlang(self):
        print(f"defualt lang is python for{self.name}")


e1=Employee("Rohan",10)
e1.showdetails()
e2=programmer("Mohan",11)
e2.showdetails()
e2.showlang()

