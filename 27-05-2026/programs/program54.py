#Write a Python program to find N largest elements from a list

numbers = [40,70,5,80,3,23,67,999,14]

n = 4

print("Largest", n, "elements are:")

numbers.sort(reverse=True)

print(numbers[:n])
