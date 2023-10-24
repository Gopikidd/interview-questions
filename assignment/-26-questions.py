# 26. Calculate the Power of a Number:
# Write a function that takes two integers as parameters, base and exponent, and calculates the base
# raised to the power of the exponent.

def power(base, exp):
    result = base ** exp
    print(f'result of the {base} power {exp} = ', result)


base_value = int(input('enter the base value = '))
exp_val = int(input("enter the power value = "))
power(base_value, exp_val)
