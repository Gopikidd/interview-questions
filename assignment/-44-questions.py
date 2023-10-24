# 44. Extract Middle Portion of a List:
# Write a Python function that takes a list as input and returns the middle portion (excluding
# the first and last third) of the list using slicing.

def middle(val):
    start = 1
    end = len(val) -1
    out = val[start:end:1]

    print('output middle string =', out)

# val = list(input('enter the value'))
val = ['gopi','surya','kidd','sakara']
middle(val)