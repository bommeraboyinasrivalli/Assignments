#Write a Python Program to find largest element in an array

arr = [20,30,5,18,45]  # Array

largest = arr[0]  # Assume first element is largest

for num in arr:   # Check each element
    if num > largest:
        largest = num

print("Largest element =", largest)
