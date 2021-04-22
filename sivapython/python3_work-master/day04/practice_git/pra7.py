num1 = float(input("enter a value:"))
op = input("enter a operator:")
num2 = float(input("enter another number:"))

if op == "+":

    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
else:
    print("wromg operator")
