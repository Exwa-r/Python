#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. 
#If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.
#initializing values to the variables





total=0

#running loop 0 to 4
for i in range (5):
    while True:
        try:
            money=int(input("Enter Your Money :"))
            #checking total is greater than 1000 or not
            if(money>=10):
                total=total+money
                print("thank you")
            #checking whether money is greater than 10 or not
            elif(money<=10):
                continue
            if(total>=1000):
                break
        except:
            print("Enter the valid Integer")
#printing total money and count
print("Total :",total)
print(f"You Have Got {i+1} ")