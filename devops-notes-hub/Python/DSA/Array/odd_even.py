arr = [10, 21, 32, 43, 54, 65]

even_count = 0
odd_count = 0

for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even elements in the array:", even_count)
print("Number of odd elements in the array:", odd_count)