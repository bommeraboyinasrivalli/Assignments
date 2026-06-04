#Write a Python program to check if the given number is Happy Number

num = int(input("Enter a number: "))

temp = num

while temp != 1 and temp != 4:
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit * digit
        temp = temp // 10

    temp = total

if temp == 1:
    print(num, "is a Happy Number")
else:
    print(num, "is not a Happy Number")
