#mthod - 1 simple loop 
arr = [1, 2, 3, 4, 5]
is_sorted = True 

for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        is_sorted = False
        break

if is_sorted:
    print("Array is sorted in ascending order")
else:
    print("Array is NOT sorted")



#Method - 2 using all() function
arr = [1, 2, 3, 4, 5]
if all(arr[i] >= arr[i - 1] for i in range(1, len(arr))):
    print("Array is sorted in ascending order")
else:
    print("Array is NOT sorted")

