def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
# Input
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

target = int(input("Enter the element to search: "))

# Verify whether the input array is sorted or unsorted
if arr == sorted(arr):
    print("Input array is sorted:", arr)
    result = binary_search(arr, target)
    if result != -1:
        print("Element found at index", result)
    else:
        print("Element not found in the list")
else:
    print("Input array is NOT sorted:", arr)
    print("Binary search requires a sorted array.")
    print("Result on unsorted array cannot be trusted. Sorting the array first...")
    sorted_arr = sorted(arr)
    print("Sorted array:", sorted_arr)
    result = binary_search(sorted_arr, target)
    if result != -1:
        print("Element found at index", result, "in the sorted array")
    else:
        print("Element not found in the list")
