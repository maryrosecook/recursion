"""Write a naive Fibonacci function recursively."""

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print fib(1)
print fib(2)
print fib(3)
print fib(4)
print fib(5)
print fib(6)
