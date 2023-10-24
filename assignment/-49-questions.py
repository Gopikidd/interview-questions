#49. Nested List to Flat List:
#If you have a nested list, you can flatten it into a single list using list comprehension.

li = ['1', '2', '3', '4', '5', ['6', '7', '8', '9']]

out = []

for i in li:
    temp = (i)
    for j in temp:
        out+= [j]

print(out)