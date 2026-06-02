a = input("Enter the value of the first variable : ")
b = input("Enter the value of the second variable : ")
# Display the original values
print(f"Original values: a = {a}, b = {b}")
# Swap the values using a temporary variable
temp=a
a=b
b=temp
# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")
