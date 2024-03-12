#Google and find the tax slabs for income tax for India. 
#Write a program to calculate the income tax for an individual.
# Input is Salary. 
#Optional input - any deductions.

income=int(input("Enter your Income per Year : "))
tax=0

if(income>0):

    if (income>300000):

       if (income>=300000 and income<=600000):
            tax= tax + 0.05*(income-300000)


       if (income>=600000 and income<=900000):
            tax= tax + 0.10*(income-600000)


       if (income>=900000 and income<=1200000):
            tax= tax + 0.15*(income-900000) 


       if (income>=1200000 and income<=1500000):
            tax= tax + 0.20*(income-1200000) 


       if(income>=1500000):
            tax= tax + 0.30*(income-1500000) 

       print(f"You have to pay  ₹{tax} as tax amount")    
    
        
    else:
          
          print(" You Don't need to pay tax👍🏻")  

else:
    print("Enter the vaild income Value")         


    
                      