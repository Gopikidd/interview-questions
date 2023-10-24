# 28. Palindrome Check:
# Write a function that checks if a given string is a palindrome (reads the same backward as forward).

def palindrome(val):
    out = ('')
    copy = val
    for i in val:
        out = i + out

    if out == copy:
        print(f'the given {copy} is palindrome')

    else:
        print(f'the given {val} is not a palindrome')


user_input = input("enter the string value :")

palindrome(user_input)
