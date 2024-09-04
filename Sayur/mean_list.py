# Given a list of numbers, calculate the average (mean) of all elements.

# numbers = [1, 2, 3, 4, 5]
# Output: 3.0

num = []
sum = 0
element = int(input("Enter the Number of elements to be added in the list : "))
for i in range(element):
    a = int(input(f"Enter the {i+1} Number on the list : "))
    num.append(a)
    sum += num[i]
    avg = sum/element

print(num)
print("Average : ",avg)