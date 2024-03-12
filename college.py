#We have 3 colleges - each college has a different cut off mark for engineering college admission.
#Get the 5 marks from the student. 
#Calculate the average.
# Find out which colleges the student is eligible to get admission.
#For eg, College 1 cut off - 93%, College 2 - 89% and college 3 - 97%. 
#If the student's avg is, 94%, the student is eligible
#for admission in College 1 and College 2



tamil=int(input("Tamil Mark : "))
english=int(input("English mark : "))
maths=int(input("Maths mark : "))
science=int(input("Science mark : "))
social=int(input("Social mark : "))


#checking every subject is between 0 to 100
if((tamil>=0 and tamil<=100) and (english>=0 and english<=100) and (maths>=0 and maths<=100) and (science>=0 and science<=100)and (social>=0 and social<=100)):

    avg=(tamil+english+maths+science+social)/5
    # sum of subject divided by number of subject 

    clg1=93
    clg2=89
    clg3=97

    print(f"Your cut off mark : {avg}")


    if(avg>=clg3 and avg>=clg2 and avg>=clg1):
        print("You are eligible for admission in College 1 and College 2 and College 3")
    elif(avg>=clg1 and avg>=clg2):
        print("You are eligible for admission in College 1 and College 2") 
    elif(avg>=clg1 and avg>=clg3):
        print("You are eligible for admission in College 1 and College 3")
    elif(avg>=clg2 and avg>=clg3):
        print("You are eligible for admission in College 2 and College 3")
    elif(avg>=clg1):
        print("You are eligible for admission in College 1 ")
    elif(avg>=clg2):
        print("You are eligible for admission in College 2 ")
    elif(avg>=clg3):
        print("You are eligible for admission in College 3 ")
    else:
        print("You are not eligible for admission") 


else:
    print("Enter the valid mark")               