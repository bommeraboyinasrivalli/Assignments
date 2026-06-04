#Write a Python program to find words which are greater than given length k

words = ["sree","sirisha","sravanthi","reshu","janaki"]

k = int(input())

result = [word for word in words if len(word) > k]

print(result)
