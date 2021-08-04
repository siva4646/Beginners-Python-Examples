year = int(input("enter a year:"))

if year % 4 != 0:
    print("not a leaf year:")
elif year % 100 != 0:
    print("this not a leaf year")
elif year % 400 == 0:
    print("leap year")
else:
    print("noty leaf year")
