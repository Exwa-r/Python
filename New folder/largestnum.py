# 3. Kth Largest Element in Array 
# Input: 
#  An integer array nums 
#  An integer k representing the kth largest element 
# Output: 
#  The kth largest element in the array nums. 
# Example: 
# Input: 
#  nums = [5,3,1,6,2] 
#  k = 3 
# Output: 3 (The third largest element is 3.) 

# Bubble sort in Python

def bubbleSort(num):
    
  # loop to access each array element
  for i in range(len(num)):

    # loop to compare array elements
    for j in range(0, len(num) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if num[j] > num[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = num[j]
        num[j] = num[j+1]
        num[j+1] = temp


num = [5,3,1,6,2]

bubbleSort(num)

k = int(input())
print(num[len(num)-k])