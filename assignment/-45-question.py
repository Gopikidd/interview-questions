# 45. Alternate Elements:
# Write a Python function that takes a list as input and returns a new list containing alternate
# elements (0-based indexing) using slicing.

def alternamtive(val):

    out = val[::2]

    print('alternative element =', out)


value = list(input('enter the list value'))

alternamtive(value)