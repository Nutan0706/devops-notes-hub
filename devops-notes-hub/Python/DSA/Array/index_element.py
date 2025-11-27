#Method 1: Linear Search (Best for interviews)
arr = [10, 21, 32, 43, 54, 65, 76, 87, 98]
target = 54
index = - 1
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break 


if index != -1:
    print("Element", target, "found at index:", index)
else:
    print("Element", target, "not found in the array")

#Method 2: Using index() method (Python built-in)

arr = [10, 21, 32, 43, 54, 65, 76, 87, 98]
target = 76
try:
    index = arr.index(target)
    print("Element", target, "found at index:", index)
except ValueError:
    print("Element", target, "not found in the array")