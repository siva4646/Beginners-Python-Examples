tuple1=(1,2,3,0,4,0,4,0,5,)
tuple1.count(0)
print(tuple1.count(0))

count=0
for i in range(0,len(tuple1)):
    if tuple1[i]==0:
        count+=1
        print(count)
    else:
        continue

print("number of zeros occured in the tuple:",count)

dict1={"name":"siva","tuple":(1,2,3,4),"list1":[2,3,4,5]}
print(type(dict1["list1"]))
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1.get("name"))
dict1.update({"sal":20})
print(dict1)

num = int(input("enter a number:"))
rem=num%2
print("reminder on deviding the number by 2:",rem)

a=int(input("enter a first number"))
b=int(input("enter second number"))
if(a>b):
    print("a is greater then b")
else:
    print("b is greater then a")


print("WELCOME STUDENTS!")
list_marks=[]
for i in range(0,6):
    print(i)
    marks=int(input("Enter marks of student: "))
    list_marks.append(marks)
list_marks.sort(reverse=False)
print("These are the marks of students in sorted order:\n", list_marks)

list1=[]
for i in range(0,7,1):
    ele=input("Enter a fruit name: ")
    list1.append(ele)
    

print(list1)
print("ensure the list of sequence object: ", type(list1))


for i in range(4, 10, 2):
    print(i)




