my_set = set()

my_list = [23,45,98,56,]

for value in my_list:
    my_set.add(value)

print(my_set)

#set will removes the duplicates
my_list1 = [12,34,54,37,43,12,12,54]
my_set = set(my_list1)
print(my_set)


def difference(n):

    if n<=17:
        return 17-n 
    else:
        return(n-17) 

print(difference(22)) 
print(difference(5)) 

#avg of two numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
avg=(a+b)/2
print("Average of 2 numbers: ", avg)




n=int(input("Enter the number of elements: "))
a=[]
for j in range(0,n):
    ele=int(input("Enter the element: "))
    a.append(ele)
    
g=a[0]
for i in range(0,len(a),1):
    if a[i]>g:
        g=a[i]
    else:
        continue

print("Greatest number: ", g)


