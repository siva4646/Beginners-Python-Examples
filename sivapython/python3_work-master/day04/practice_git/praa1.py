import datetime
str1='''Dear NAME,
Congratulations, You got selected!
Thank you!
Undersigned
DATE
'''
name = input("Enter your name: ")
d = str(datetime.datetime.now())
str1=str1.replace("NAME", name)
str1=str1.replace("DATE", d)
print(str1)

list1=[]

num=int(input("Enter number of elements you want add: "))
for i in range(0,num):
    ele=int(input("Enter a number: "))
    list1.append(ele)

print("Sum of numbers in the list: ", sum(list1))

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=a+b
print(c)
