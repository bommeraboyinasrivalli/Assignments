#Write a Python Program to Find the Sum of Natural Numbers

num=int(input("enter the number:"))
sum=0
for i in range(1,num+1):
    sum+=i
print(f" sum of natural numbers upto",num,"is",sum)
