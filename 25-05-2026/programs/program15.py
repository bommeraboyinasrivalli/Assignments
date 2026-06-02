#Write a Python Program to Print all Prime Numbers in an Interval of 1-10

print("prime numbers between 1 to 10 are :")
for num in range(1, 11):
    count = 0



    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num)
