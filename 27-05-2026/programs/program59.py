#Write a Python program to Count occurrences of an element in a list

# Count occurrences of an element in a list

def count_occurrences(l, element):
     count = l.count(element)
     return count

my_list = [10,20,30,30,50,50,40,30,20,30,80,30,70]

element_to_count = 30

occurrences = count_occurrences(my_list, element_to_count)

print(f"The element {element_to_count} appears {occurrences} times in list")
