def max_num(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return  num1
    if num2 < num3 and num3 < num1:
        return num2
    else:
        return num3 

print(max_num(54,10,90))
