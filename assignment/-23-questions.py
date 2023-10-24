# 23. Reverse a String:
# Write a function to reverse a given string.
def reverse(val):
    out = ' '
    for i in val:
        out = i+out
    return out


value = input('enter the string =')
print('original string =', value)
print('reversed string =', reverse(value))

