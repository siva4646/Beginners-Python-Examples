class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname



    def printname(self):
        print("im here")
        print(self.name, self.surname)



        
x = Person("siva", "bommisetty")
#print(x)
x.printname()
