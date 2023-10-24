# 27. Find the Maximum Number:
# Write a function that takes an array of numbers as input and returns the maximum number in the
# array.

def maximum(li):
    max_val = li[0]
    for i in li:
        if i > max_val:
            max_val = i
    return max_val


lis = [1, 22, 33, 44, 556, 999]

print('maximum value of the list = ', maximum(lis))
