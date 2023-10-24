##50. List of Dictionaries to Dictionary of Lists:
# If you have a list of dictionaries where each dictionary represents a person and contains
# information like name, age, etc., you can convert it to a dictionary of lists grouped by keys
# (e.g., 'name', 'age')
li1 = ['gopi', 'surya', 'sakara', 'karuppu']
li2 = [1, 2, 3, 4]

result = {}
for i in range(len(li1)):
    result[li2[i]] = li1[i]

print('List to Dictionary:', result)

lis1 = list(result.keys())
lis2 = list(result.values())

print('lis1 =', lis1)
print('lis2 =', lis2)
