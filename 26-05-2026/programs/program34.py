#Write a Python Program for array rotation.


def rotate_array(arr, d):
    n = len(arr)

    rotated_arr = [0] * n

    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]

    return rotated_arr


arr = [1, 2, 3, 4, 5]
d = 2

result = rotate_array(arr, d)

print("Original Array:", arr)
print("Rotated Array:", result)
