
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("siva", 34)

print(p1.name)
print(p1.age)


class person:
    

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def myfun(self):
        print("my name is ",self.name)
        

p1 = person("john", 25)
p1.myfun()
p1.age = 25
print("my age is", 25)


class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, self.age)

class student(person1):
    def __init__(self, name, age):
        person1.__init__(self, name, age)

x = student("siva", 24)
x.printname()



class person2:
    def __init__(self, dept,course):

        self.dept = dept
        self.course = course

    def cls(self):
        print(self.dept, self.course)

class student1(person2):
    def __init__(self, dept, course):
        person2.__init__(self, dept, course)

x = student1("mca", "mca1")
x.cls()


class person2:
    def __init__(self, dept,course):

        self.dept = dept
        self.course = course

    def cls(self):
        print(self.dept, self.course)

class student1(person2):
    def __init__(self, dept, course):
        super().__init__(dept, course)

x = student1("mca", "mca1")
x.cls()

class person3:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def cls1(self):
        print(self.fname, self.lname)

class student2(person3):
    def __init__(self, fname, lname, month):
        super().__init__(fname, lname)
        self.month = 3

    def welcome(self):

        print("welcome", self.fname, self.lname, "to office", self.month)


x = student2("siva", "bommisetty", "month")
x.welcome()

myiter = ("banana","apple","graps")
miter = iter(myiter)

print(next(miter))
print(next(miter))
print(next(miter))

myter1 = ("banana")
miter1 = iter(myter1)

print(next(miter1))
print(next(miter1))
print(next(miter1))

mytuple = ("rock","snow","chew")

for x in mytuple:
    print(x)

x.count(x)

class MyNumbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a 
        self.a += 15
        return x

mynum = MyNumbers()
myiter2 = iter(mynum)

print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))


class MyNumbers1:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myiter3 = MyNumbers1()
myiter = iter(myiter3)

for x in myiter3:
    print(x)
        
num = int(input("enter a number:"))

if (num % 2) == 0:
    print("given number is even number",num)
else:
    print("given number is odd",num)

num = 6

factorial = 1

if num < 0:
    print("negative numbers doesnot allow")
elif num == 0:
    print("zero factorial is 1")
else:

    for i in range(1, num + 1):
        factorial = factorial*1
        print("the factorial", num , "is", factorial)
  






















