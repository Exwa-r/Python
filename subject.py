# If the mark is greater than 75 in any two subjects, 
#then print Pass and also print the subject where the marks is > 75
# If the marks is greater than 60 in all three subjects, then print pass.
#  If the student scored in 100 in any one subject, it is pass.
# Print which subject the student scored 100.
# if the above conditions  not met, print fail.




maths=int(input("Enter Your Maths mark : "))
science=int(input("Enter Your Science mark : "))
social=int(input("Enter Your Social mark : "))


if (maths==100 or science==100 or social==100):
    if(maths==100):
        print(f"You have scored {maths} in Maths")
    if(science==100):
        print(f"You have scored {science} in Science")
    if(social==100):
        print(f"You have scored {social} in Social") 
    print("Pass")


elif ((maths>=75 and science>=75) or (maths>=75 and social>=75) or (science>=75 and social>=75)):
    if (maths >= 75):
        print(f"You have Scored {maths} marks in Maths")
    if (science >= 75):
        print(f"You have Scored {science} marks in Science")
    if (social >= 75):
        print(f"You have Scored {social} marks in Social")
    print("Pass")

elif(maths>60 and science>60 and social>60 ):
    print("Pass")
    
else:
    print("Fail")                   


    
