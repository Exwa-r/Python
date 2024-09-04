# 1. Find the Missing Number 
# Input: 
#  An integer array nums containing n distinct numbers from the range 0 to n-1 
# Output: 
#  The missing number in the array nums. 
# Example: 
# Input: nums = [3,0,1] 
# Output: 2 (Since 2 is missing from the range 0 to 2) 


num = [0,2,5,9,1,4,7]
greater = num[0]
lesser = num[0]

for i in range(len(num)):
    
    if (greater < num[i]):
        greater = num[i]
    
    if (lesser > num[i]):
        lesser = num[i]

for lesser in range(greater):
    if (lesser not in num):
        print(lesser)
