#Write a Python Program for cube sum of first n natural numbers

n = int(input("Enter a number: "))

cube_sum = 0

for i in range(1, n + 1):
    cube_sum = cube_sum + i**3

print(f"The cube sum of the first {n} natural numbers is:", cube_sum)
