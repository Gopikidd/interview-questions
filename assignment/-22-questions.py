# 22. Sum of Natural Numbers:
# Write a function to find the sum of natural numbers up to a given number n.

def sum_natural(start, end):
    sume = 0
    for i in range(start, end+1):
        sume += i
    if sume >= 1:
        return sume


start = int(input('enter the starting number = '))
end = int(input('enter the ending number'))
result = sum_natural(start, end)
print(f'sum of {start} to {end} numbers =', result)
