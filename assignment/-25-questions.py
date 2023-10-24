# 25. Fibonacci Series:
# Write a function to generate the Fibonacci sequence up to a certain number of terms.

def fibonacci(rang):
    fib1 = 0
    fib2 = 1
    fib3 = fib1 + fib2
    i = 1
    while rang >= i:
        print(i, 'fib value =', fib3)
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2
        i += 1


rang = int(input('enter the value = '))
fibonacci(rang)




