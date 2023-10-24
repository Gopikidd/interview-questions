# 42. Extract Last N Elements:
# Write a Python function that takes a list and an integer n as input and returns the last n
# elements of the list using slicing

def last_element(val):
    val1 = str(val)
    out = val1[-1::]

    print('NTH ELEMENT OF INTEGER LIST = ', int(out))




val = int(input('enter the integer = '))

last_element(val)