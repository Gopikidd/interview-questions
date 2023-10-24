# 40. Extract Even-Indexed Characters:
# Write a Python function that takes a string as input and returns a new string containing only
# the characters at even indices (0-based indexing) using slicing.

def even_char(val):
    out = val[::2]

    print('even index char =', out)

value = input('enter the string =')

even_char(value)