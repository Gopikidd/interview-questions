# 43. Remove Duplicates from List:
# Write a Python function that takes a list as input and returns a new list with duplicates
# removed using slicing.

def duplicate (val):
    remove_dup = []
    for i in val:
        temp = i

        if temp not in remove_dup:
            remove_dup.append(temp)

    print('rempve_duplicte = ', remove_dup)


# val = list(input('enter the list value ='))
val = ['apple', 'apple', 'orange', 'orange', 'goa', 'orange', 'goa', 'goa']
duplicate(val)

