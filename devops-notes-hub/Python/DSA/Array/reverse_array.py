#method 1: Using slicing
arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left] , arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed array is:", arr)

#method : 2 built-in function

arr = [1, 2, 3, 4, 5]
arr.reverse()
print("Reversed array is:", arr)