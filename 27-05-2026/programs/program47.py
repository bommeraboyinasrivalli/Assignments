#Write a Python program to determine whether the given number is a Harshad Number

num = int(input("Enter a number: "))

s = sum(int(i) for i in str(num))

if num % s == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")

