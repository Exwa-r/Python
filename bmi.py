print("BODY MASS INDEX")

cm=float(input("Enter your height in Centimeter : "))
kg=float(input("Enter your weight in kilogram : "))


if ((cm>0 and cm<=250) and (kg>0 and kg<=250)):

    #converting centimeter into meter
    m=cm/100      
   

    #calculatinh bmi
    bmi=kg/(m*m) 
    
      
    print(f"Your BMI : {bmi}")
   
    #Calculating and finding bmi range
    
    if(bmi<18.5):
        print("Under weight")
    elif(18.5 <= bmi and bmi <=24.9 ):
        print("Healthy weight")
    elif(25<=bmi and bmi <=29.9):
        print("Over weight")
    elif(bmi>=30):
        print("Obese")
    else:
        print("Several Obese")    

else:
    print("Enter valid height and weight!!")
