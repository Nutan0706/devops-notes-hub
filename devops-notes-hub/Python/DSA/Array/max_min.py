arr = [10, 21, 32, 43, 54, 65, 76, 87, 98]

min = float('inf')

for num in arr:
    if num < min:
        min = num 

print("The minimum element in the array is:", min)

max = float('-inf')

for num in arr:
    if num > max:
        max = num

print("The maximum element in the array is:", max)