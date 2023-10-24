# 20. Check Even or Odd:
# Write a function that takes an integer as input and returns "Even" if the number is even and "Odd" if
# it's odd.

def odd_even(i):
    if i % 2 == 0:
        print(f'the given {i} is even')
    else:
        print(f'the given {i} is odd')


lis = int(input('enter the integer = '))

odd_even(lis)
