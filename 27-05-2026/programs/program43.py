#Write a Python program to check if the given number is a Disarium Number

num = int(input("Enter a number: "))

num_str = str(num)
sum = 0

for i in range(len(num_str)):
    digit = int(num_str[i])
    sum = sum + digit ** (i + 1)

if sum == num:
    print(num, "is a Disarium Number")
else:
    print(num, "is not a Disarium Number")
