num = int(input("enter the value"))
rang = int(input("enter the range"))
out = 1
li = []
for i in range(1, rang+1):
    out = out*num
    li.append(out)
print(li)

