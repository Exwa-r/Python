#Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or mininum.
#Find the answer and print.


num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
num3=int(input("Enter the third number : "))

choice=int(input("Enter 1 for Maximum or 2 for Minimum : "))

if(choice==1): #maximum works
    if(num1>num2 and num1>num3):
        print(f"{num1} is Maximum")
    elif(num2>num3):
        print(f"{num2} is Maximum")   
    else:
        print(f"{num3} is Maximum")     
elif(choice==2): #minimum works
    if(num1<num2 and num1<num3):
        print(f"{num1} is Minimun")
    elif(num2<num3):
        print(f"{num2} is Minimum")   
    else:
        print(f"{num3} is Minimum")
else:
    print("Enter the Correct choice 1 or 2")

    