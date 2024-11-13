def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_series_recursive(n):
    fib_series = [fibonacci_recursive(i) for i in range(n+1)]
    return fib_series

# Get dynamic input from the user
n = int(input("Enter a number to calculate Fibonacci series up to: "))
print(f"Fibonacci series up to {n}: {fibonacci_series_recursive(n)}")
