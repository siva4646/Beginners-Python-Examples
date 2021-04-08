#author siva
#basic functios with and without arguments

def myfunc():
    print('my function created')
    
myfunc()

def myfunc1(fname):
    print(fname    +" "      'sairu')

myfunc1('email')
myfunc1('gmail') 
myfunc1('siva') 

def myfunc2(sname , name):
    print(sname + " "+ name)

myfunc2("giri","suri")

def my_func(*args):
    print("my age is:" +args[0])

my_func("suri","giri","puri")

def my_func1(child1,child2,child3):
    print("my age is " + child2)

my_func1(child1="siri",child2="puri",child3="sari")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def myfunc6(food):
    for x in food:
        print(x)

fruits = ["apple","banana","graps"]

myfunc6(fruits)



