#method :1 two pointer approach 
def move_zeros(arr):
    j = 0

    # step 1: move all non-zero elements to the front 
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    # step 2: fill remaining positions with zeros
    while j < len(arr):
        arr[j] = 0
        j += 1
    return arr 

# Example usage:
arr = [0, 1, 0, 3, 12]
print(move_zeros(arr))

