# Count Vowels:
# Write a Python program that counts the number of vowels (a, e, i, o, u) in a given string 
# using a for loop.


vowels = ['a','e','i','o','u']
count = 0
char = input("Enter a String : ").lower()

for i in char:
    if i in vowels:
        count += 1

print(count)