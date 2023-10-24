# 21. Factorial Calculation:
# Write a function to calculate the factorial of a non-negative integer.

def factorial(val):
    fact = 1
    num = 1
    while val >= num:
        fact = fact * num
        num += 1
    return fact


value = int(input('enter the input = '))
result = factorial(value)
print(f'{value} factorial value = ', result)

