#addition
num1=float(input("enter the num1:"))
num2=float(input("enter the num2:"))
sum=num1+num2
print(f"sum:{num1}+{num2}={sum}")
#division
num3=float(input("enter the num1:"))
num4=float(input("enter the num2:"))
if num4 == 0:
    print("Error: Division by zero is not allowed.")
else:
    div_result = num3 / num4
    print(f"Division: {num3} / {num4} = {div_result}")
