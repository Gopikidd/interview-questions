# 34. Reverse Words in a String:
# Write a function that reverses the order of words in a given string

def reverse_str(val):
    va = val.split(' ')
    out = va[::-1]
    out1 = ' '.join(out)

    print('reverse string element = ', out1)


user_input = 'python is a programming language'
reverse_str(user_input)
