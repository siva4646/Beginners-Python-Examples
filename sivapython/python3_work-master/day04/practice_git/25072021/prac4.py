num = 6
factorial = 1
if num < 0:
    print("negative numbers doesnot allow")
elif num == 0:
    print("zero factorial is 1")
else:
    for i in range(1, num + 1):
        print(i)
        factorial = factorial*i
print("the factorial", num , "is", factorial)

