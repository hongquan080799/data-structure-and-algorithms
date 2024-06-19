def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
array = [2, 4, 0, 1, 9]
target = 1
result = linear_search(array, target)
print(f"Element found at index: {result}")
