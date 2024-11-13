#include <iostream>
using namespace std;

// Non-recursive (iterative) Fibonacci function
int fibonacci_iterative(int n) {
    if (n <= 1)
        return n;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

// Recursive Fibonacci function
int fibonacci_recursive(int n) {
    if (n <= 1)
        return n;
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

int main() {
    int n;
    cout << "Enter the position of Fibonacci number: ";
    cin >> n;

    // Calculating Fibonacci number iteratively
    cout << "Iterative Fibonacci of " << n << " is: " << fibonacci_iterative(n) << endl;

    // Calculating Fibonacci number recursively
    cout << "Recursive Fibonacci of " << n << " is: " << fibonacci_recursive(n) << endl;

    return 0;
}

/*
Recursive fibbonacci:
Time Complexity: O(n*2n)
Auxiliary Space: O(n), For recursion call stack.

Iterative fibbonacci:
Time Complexity: O(n) 
Auxiliary Space: O(1)
*/