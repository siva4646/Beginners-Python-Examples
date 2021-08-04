


f = open("E:\starting _basics/basic.txt","r")
print(f.read())


f = open("E:\starting _basics/basic.txt","a")
f.write("sunday is cool!")
f.close()


f = open("E:\starting _basics/basic.txt","rt")
print(f.read())
f = f.read()
words = f.split()

print("the number of words in text file",len(words))


f = open("E:\starting _basics/basic.txt","rt")
print(f.read)


f1 = open("E:\starting _basics/basic.txt","rt")
f2 = open("E:\starting _basics/basic.txt","wt")
for line in f1:
    f2.write(line.replace("sunday","siva"))
    f1.close()
    f2.close()









