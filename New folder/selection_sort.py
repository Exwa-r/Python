def selectionsort(num):
    
  
  for i in range(len(num)):


    for j in range(i, len(num)):
      
      if num[i] > num[j]:

        temp = num[i]
        num[i] = num[j]
        num[j] = temp


num = [64, 25, 12, 22, 11]

selectionsort(num)
print(num)