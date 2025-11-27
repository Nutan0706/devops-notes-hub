#Method 1: Using max() (Pythonic way)
arr = [12, 45, 7, 99, 23]
largest = max(arr)
print("Largest element using max():", largest)

#Method 2: without using max() manually loop

arr = [12, 45, 7, 99, 23]
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num 

print("Largest element using loop:", largest)
