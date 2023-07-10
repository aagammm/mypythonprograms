class Person:
    name="Aagam"
    occupation="Engineer"
    age=42
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a=Person()
a.name="Pratham"
a.occupation="Doctor"
a.age=45
a.info()


