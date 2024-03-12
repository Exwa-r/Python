#The user just bought a few things in your  shop. 
#Ask the user what he bought. 
#Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. 
#Calculate the total cost.
#Ask the user to pay the amount. 
#Receive the amount from the user (get money as input). 
#Print the change amount you have to give to the user. 
#Hint - use float datatype




a=0
b=0
c=0
vadai = 20
soda = 30
sandwich = 100

getvadai=float(input("Number of vadai: "))
getsoda=float(input("Number of Soda: "))
getsandwich=float(input("Number of sandwich: "))

if(getvadai>=0 and getsoda>=0 and getsandwich>=0):
    if (getvadai!=0 or getsoda!=0 or getsandwich!=0 ):
        a=getvadai*vadai
        b=getsoda*soda
        c=getsandwich*sandwich  
    
        total=a+b+c

        amount=int(input(f"Your Bill: ₹{total}  Give your amount : "))
    
        if(amount>total):
            balance=amount-total
            print(f"Get your balance amount : ₹{balance} ")  
            print("Thank you ")
        elif(amount<total):
            remains=total-amount
            print(f"Please pay your balance amount : ₹{remains} ")
        else:
            print("Thank you ")
    
    else:
        print("Request U to buy some dish")
else:
    print("Enter a Valid amount")        

   

