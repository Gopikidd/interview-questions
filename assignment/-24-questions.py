# 24. Check for Prime Number:
# Write a function that checks if a number is prime or not.

def prime(val):
    num = 2
    while val > num:

        if val % num == 0:
            print(f'{val} number is not a prime ..........! ')
            break
        num += 1

    else:
        print(f'{val} is a prime')


number = int(input('enter the value = '))
prime(number)
