# Count occurences of character
# Eg:
# String: hello
# Character: l

# output=2

# i=0
# count=0
# string=input("String : ")
# char=input("Character : ")

# while i < len(string):
#     if char == string[i]:
#         count += 1
#     i += 1

# print(count)


# Count words in a sentence
# Input: Python is a powerful programming language
# Output: 6
count = 0
string=input("String : ").split()
for word in string:
    count += 1
print(count)
print(len(string))
print(string)

