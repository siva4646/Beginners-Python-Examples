f = open ("E:/file/pta.txt","r")
print(f.read())

f = open ("E:/file/pta.txt","r")
print(f.readline())

f = open ("E:/file/pta.txt","r")
print(f.read())

class Employee:
    EmpCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = name
        Employee.Count +=1


    def displayCount(self):
        
        print("Total Employee %d" % Employee.EmpCount)
    def EmployeeCount(self):
        print("name :",self.name,"age",self.age)
        emp1 = ("siva",25)
        emp2 = ("ram",34)
        emp1.displayEmployee()
        emp2.displayEmployee()
        
        print("Total Employee %d" % Employee.EmpCount)



    


