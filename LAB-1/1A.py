def countdown(n):
    if n == 0:
        print("Launch!")
    else:
        print(n)
        countdown(n - 1)

# Input
n = int(input("Enter countdown number: "))

# Function call
countdown(n)