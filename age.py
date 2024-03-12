#Calcualte and print users age - 
#Write a program to ask the user for his/her name and print 'Hello', user's name. 
#Ask what year they were born.  
#get the year from the user. 
#Print 'You are <age> years old'.


name=input("Enter your name : ")
print(f"Hello,{name}")
year=int(input("Enter the year you were born 1920 to 2024: "))


if (year>=1920 and year<=2024):
    age=2024-year
    print("You are ",age," years old")
else:
    print("Enter the vaild birth year between 1920 to 2024")    


