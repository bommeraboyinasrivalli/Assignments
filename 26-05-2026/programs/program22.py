#Write a Python Program to Find LCM.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = a

while lcm % b != 0:
    lcm = lcm + a

print("LCM =", lcm)
