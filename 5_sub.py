#write code for both for and while loop
#Get marks from 5  students and calculate avg


# #for loop
total = 0
count=1

for i in range (5):
    while True:
        try:
            mark=int(input(f"Enter {count} Student mark : "))

            if(mark>=0 and mark<=500):
                count += 1
                break
        
            else:
                print("Enter the valid Mark 0 to 500 ")  

        except:
            print("Enter the Valid Integer")        
    total += mark
#print(total, "/5")      20+30+40+50+60/5            
avg=total/5

print ("Avg is : ", avg )

# using while loop

total = 0
count = 1
noOfStudents = 5
i = 0
while (i < noOfStudents):
    while True:
        try:
            mark=int(input(f"Enter {count} Student mark : "))

            if(mark>=0 and mark<=500):
                count += 1
                break
            else:
                print("Enter the valid Mark 0 to 500 ")

        except :
            print("Enter the Vaild integer")
        
        
    total += mark
    i += 1
avg=total/5        
print ("Avg is ", avg)