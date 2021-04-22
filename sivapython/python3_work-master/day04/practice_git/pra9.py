import sys
randomlist = ['a',0,3,4]

for entry in randomlist:
    try:
        print("the num is entry",entry)
        r = 2/int(entry)
        print("value of",r,"is")
        break
    except:
        print("the num is not correct", entry)
        print("next entry")
        print()
        
print("the reciprocal of",entry,"is", r)




