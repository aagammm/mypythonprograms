class Person:
    def __init__(self,name,occ):
        self.name=name
        self.occ=occ

    def info(self):
        print(f"{self.name} is a {self.occ}")
    

a=Person("Aagam","Developer")
b=Person("Pratham","doctor")
a.info()
b.info()

        
        