#method : 1 using slicing 
def rotate_right(arr, k):
    k = k % len(arr)  
    return arr[-k:] + arr[:-k]

print(rotate_right([1, 2, 3, 4, 5, 6, 7], 3))


def rotate_left(arr, k):
    k = k % len(arr)  
    return arr[k:] + arr[:k]

print(rotate_left([1, 2, 3, 4, 5, 6, 7], 3))

#in-place rotation 
def rotate_right(arr, k):
    k = k % len(arr)

    #revese full array 
    arr.reverse()

    #reverse first k elements
    arr[:k] = reversed(arr[:k])

    #reverse remaining elements
    arr[k:] = reversed(arr[k:])
    return arr

print(rotate_right([1, 2, 3, 4, 5, 6, 7], 3))


#left rotation in place
def rotate_left(arr, k):
    k = k % len(arr)

    #reverse first k elements
    arr[:k] = reversed(arr[:k])

    #reverse remaining elements
    arr[k:] = reversed(arr[k:])

    #reverse full array
    arr.reverse()
    return arr

print(rotate_left([1, 2, 3, 4, 5, 6, 7], 3))