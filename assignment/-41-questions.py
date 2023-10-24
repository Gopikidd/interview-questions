# 41. Reverse a List Using Slicing:
# Write a Python function that takes a list as input and returns the list reversed using slicing.

def reverse(val):
    out = val[::-1]

    print('reverse list =', out)



value = ['python', 'java', 'sql', 'html', 'css']
# value = list(input('enter the string'))
print('original list =', value)

reverse(value)