class Employee:
    EmpCount = 0

    def __init__(self, name, salery):
        self.name = name
        self.salery = salery
        Employee.EmpCount +=1
        


    def displayCount(self):
        print("Total Employee %d" % Employee.EmpCount)

    def displayEmployee(self):
        print("name :", self.name,",salery",self.salery)

emp1 = Employee("siva",25)
emp2 = Employee("ram",34) 
emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee %d" % Employee.EmpCount)




