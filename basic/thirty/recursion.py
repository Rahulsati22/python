# factorial of a number
def factorial(n):
    if (n == 1 or n == 0):
        return n

    return n * factorial(n-1)


# fibonacci number
def fibo(n):
    if (n == 1):
        return 0
    if (n == 2 or n == 3):
        return 1
    n = fibo(n-1) + fibo(n-2)
    return n

# ans = factorial(100);
# print(ans);


ans = fibo(10)
print(ans)
