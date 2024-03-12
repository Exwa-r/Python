#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000.
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones
# this month also, then he gets additional Rs5000.



base_monthly_salary=10000
phoneCount=0
first_five_phone_bonus =5000
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
monthlySalesList = []
# 5,23,21,14,23,12,4,12,22,22,34,12
monthly_Salary_List = [] 
yearly_salary=[]               #[20000,37000,10000,54000]
# Sample number of phones sold in each month in a year
#FillinMissingCode - initialise all the variables needed

for month in range (12):
    while True:
        try:
            phone=int(input(f"Enter the phone count you sold on {months[month]} : "))
            if (phone > 0):
                break
            else:
                print("Enter the vaild Phone Count You have Sold") 
        except ValueError:
            print("Enter the Vaild integer")
    monthlySalesList.append(phone)

print("############################################################") 
print("\nMONTHLY SALARY LIST\n")
for month,phoneCount in enumerate(monthlySalesList):
    
    #calculate the Salary using If stmts
        if (phoneCount == 5):
            base_monthly_salary += first_five_phone_bonus
            print(f"your salary for {months[month]} is: {base_monthly_salary}")
            monthly_Salary_List.append(base_monthly_salary)
            base_monthly_salary = 10000


        elif(phoneCount > 5):
            base_monthly_salary += first_five_phone_bonus
            base_monthly_salary += (phoneCount - 5) * 1100
            print(f"your salary for {months[month]} is: {base_monthly_salary}")
            monthly_Salary_List.append(base_monthly_salary)
            base_monthly_salary = 10000

        else:
            base_monthly_salary = 10000
            print(f"your salary for {months[month]} is: {base_monthly_salary}")
            monthly_Salary_List.append(base_monthly_salary)

    
        
        
print("############################################################\n") 
print("############################################################")        
print("\nAdditional salary for good performance in previous month\n")


for month in range(12):
    if month == 0:
        continue
    
    
    elif monthly_Salary_List[month-1] > 20000 and monthlySalesList[month-1] >= 20:
        print(f"✨Additional salary for {months[month-1]} performance 5000✨")
        total_salary = monthly_Salary_List[month]+5000
        print(f"✨your total salary for {months[month]} is: {total_salary}✨\n" )
        


    else:
        print(f"You Have not Selled 20 phones in {months[month-1]} To Get Bonus\n")
        

print("############################################################")  






