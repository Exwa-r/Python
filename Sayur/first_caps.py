# Title Case Conversion:
# Write a Python program that converts the first letter of each word in
# a given sentence to uppercase (title case).


string = input("Enter the String : ").split()
caps = ""

for word in string:
    caps += word.capitalize()+" "
print(caps)