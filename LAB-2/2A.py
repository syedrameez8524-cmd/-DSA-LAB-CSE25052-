def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Input
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

target = int(input("Enter the element to search: "))

# Function call
result = linear_search(arr, target)

# Output
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found in the list")
