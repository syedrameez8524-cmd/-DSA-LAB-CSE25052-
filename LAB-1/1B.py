def power(p, n):
    if n == 0:
        return 1
    else:
        return p * power(p, n - 1)

# Input
p = int(input("Enter principal growth factor: "))
n = int(input("Enter number of years: "))
# Function call
result = power(p, n)

# Output
print("Power =", result)
