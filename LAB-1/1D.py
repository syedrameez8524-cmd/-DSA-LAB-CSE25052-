def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Input
n = int(input("Enter a number to find its factorial: "))
# Function call
print("Factorial of", n, "is", factorial(n))
