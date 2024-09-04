# Count Words:
# Write a Python program that counts the number of words in a given sentence.

count = 0

string = input("Enter your String : ").split()
for i in string:
    count += 1
print(f"Number of Words in string : {count}")
