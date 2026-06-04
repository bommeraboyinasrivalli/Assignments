#write a Python program to print all pronic numbers between 1 and 100.

print("Pronic numbers between 1 and 100:")

for i in range(1, 100):
    if i * (i + 1) <= 100:
        print(i * (i + 1), end=" | ")
