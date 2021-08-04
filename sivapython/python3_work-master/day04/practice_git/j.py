import json


x = '{"name":"john", "age":30, "city":"kadapa"}'

y = json.loads(x)

print(y["age"])

print(y)

import json

x = {
    "name":"siva",
    "age":45,
    "code":1234
}
y =json.dumps(x)

print(y)


import json

x = {
    "name" : "siva",
    "age" : 30,
    "gender" : "male",
    "cars" : [
        {"model":"bmw", "number":1223, "price":32933},
        {"model":"audi","number":838,"price":29383}
    ]
}
y = json.dumps(x)

print(y)

class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):

        print(self.firstname,self.lastname)

x = Person("John", "Doe")
x.printname()



