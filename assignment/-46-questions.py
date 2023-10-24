# 46). List of Strings to List of Unique Characters:
# If you have a list of strings and you want to get a list of unique characters from all the
# strings

li = ['apple','orange','banana','cherry','dragon fruit']

out = []

for val in li:
    for j in val:
        if j not in out and j !=' ':
            out+= [j]

print('unique value = ', out)