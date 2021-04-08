#python function with examples

def myfunc1(country = "newziland"):
    print("i am from" " " +   country)

myfunc1("india")
myfunc1("south")
myfunc1()
myfunc1("arab")

def myfunc2(x):
    return 5 * x

print(myfunc2(3))
print(myfunc2(4))
print(myfunc2(5))

def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nrecursion example results")
tri_recursion(8)

#python lambda topic

x = lambda a : a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

def myfunc3(n):
      return lambda a : a * n
mydouble = myfunc3(2)


print(mydouble(11))

