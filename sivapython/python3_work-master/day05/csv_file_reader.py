

#file = open("google_stock_data.csv")
"""for line in file:
    print(line)
    
    """

lines = [line for line in open("E:/Ptyhonexample/Beginners-Python-Examples/sivapython/python3_work-master/day05/google_stock_data.csv")]
#print(lines)
one=lines[1].strip()
print(one.split(","))


csv = lines[0].strip().split(",")

print(csv)