# 31. Find Missing Number:
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, write a function to find
# the one that is missing from the array.
def missing(num):
    missing = []
    for i in range(1, 11):
        if i not in number:
            missing += [i]

    return missing

number = [1, 2, 3, 4 , 5, 6, 8, 9]

print('given number = ', number)

print('missing number = ', missing(number))