# Given a list of numbers, find the maximum element.

# Example usage:
# numbers = [3, 7, 2, 8, 5]
# Output: 8


num = []

element = int(input("Enter the Number of elements to be added in the list : "))

num.append(int(input("Enter the 1 Number on the list : ")))
great = num[0]

for i in range(1,element):
    num.append(int(input(f"Enter the {i+1} Number on the list : ")))
    if great < num[i]:
        great = num[i]

print(num)
print(great)


# num = []

# element = int(input("Enter the Number of elements to be added in the list : "))

# for i in range(element):
#     a = int(input("Enter the : "))
#     num[i] = a

# great = num[0]
# for i in range(1,element):
#     if great < num[i]:
#         great = num[i]

# print(num)
# print(great)