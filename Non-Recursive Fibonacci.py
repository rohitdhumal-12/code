def fibonacci_non_recursive(n):
    fib_series = []
    if n >= 0:
        fib_series.append(0)
    if n >= 1:
        fib_series.append(1)
    
    fib_0, fib_1 = 0, 1
    for i in range(2, n+1):
        fib_n = fib_0 + fib_1
        fib_series.append(fib_n)
        fib_0 = fib_1
        fib_1 = fib_n

    return fib_series

# Get dynamic input from the user
n = int(input("Enter a number to calculate Fibonacci series up to: "))
print(f"Fibonacci series up to {n}: {fibonacci_non_recursive(n)}")
