arr = [12, 24, 7, 99, 23, 99]

largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest 
        largest = num 

    elif num > second_largest and num != largest:
        second_largest = num 

if second_largest == float('-inf'):
    print("No second largest element")
else:
    print("The second largest element is:", second_largest)