# Get the input from use list of words. Find the words that have the same unique letters.
# Count the repeted unique letters and print the number of repetitions.

# If  input = ["abc", "aabbcc", "good", "god", "abbcc", "fyg"]

# output = [a,b,c]  = 3 times 

# [g,o,d] = 2 times

# Words with Duplicate Letters:
# Write a Python program that identifies and prints all words in a given sentence that contain duplicate letters.

# Words with Common Letters:
# Write a Python program that identifies and prints all pairs of words in a given list of words that have at least one common letter.

# Words with Maximum Length:
# Write a Python program that finds and prints all words in a given list of words that have the maximum length.

# Try all the above homework problems, this will give you good practice with string and list manipulations in python



# input = ["abc", "aabbcc", "good", "god", "abbcc", "fyg"]
# new_char = ''
# new = []

# for word in input:                            #abc               
#     for i,char in enumerate(word):            #word[0] == word[i+1]
#         for j in range(len(word)):
#             if word[i] not in word[j]:
#                 new_char += word[i]
                
#     new.append(new_char)
# print(new)



# Homework problem: Get the input from use list of words. Find the words that have the same unique letters.
# Count the repeted unique letters and print the number of repetitions.
# If  input = ["abc", "aabbcc", "good", "god", "abbcc", "fyg"]
# output = [a,b,c]  = 3 times

# [g,o,d] = 2 times
# Words with Duplicate Letters:
# Write a Python program that identifies and prints all words in a given sentence that contain duplicate letters.
# Words with Common Letters:
# Write a Python program that identifies and prints all pairs of words in a given list of words that have at least one common letter.
# Words with Maximum Length:
# Write a Python program that finds and prints all words in a given list of words that have the maximum length.
# Try all the above homework problems, this will give you good practice with string and list manipulations in python

list1 = ["abc", "aabbcc", "good", "god", "abbcc", "fyg"]
remove_list=[]
str=""
d=""
new = []

# list_count = int(input("Enter how many elements you are going to get in the list: "))

# for i in range(list_count):
#     get_element = input("Enter the element: ")
#     list1.append(get_element)
# print(list1)

for index,word in enumerate(list1):
    for j in word:
        if j not in str:
            str=str+j
    remove_list.append(str)
    str=""

print(remove_list)

count=0
for i in range(len(remove_list)):
    for i,word in enumerate(remove_list):
        if word in remove_list[i+1:]:
            count +=1
    print(count)        
    if count >  1:
        new.append(word)
print(new)
count = 0

for letter,j in enumerate(remove_list):
    for index,k in enumerate(remove_list):
            if(j in k):
                count+=1
                letter+=1
    
    if(count>=1):
        if(j not in d ):
            d=j
            print(j,"-",count)
             
    count=0
