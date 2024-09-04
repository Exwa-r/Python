# Write a Python program that prompts the user to enter a password until a valid password 
# (at least 8 characters long and 
#  containing at least one uppercase letter, 
#  one lowercase letter, one digit, and 
#  one special character) is entered. 
# Use a while loop.


i=0

symbols = ['@','#','$','%','^','&','*','(',')','!',',','.','[',']','{','}']
while True:
    upper=False
    lower=False
    number=False
    sym=False
    password = input("Enter your password : ")
    if len(password) >= 8 :
        while i<len(password):
            if password[i].isupper():
                upper = True
            elif password[i].islower():
                lower = True
            elif password[i].isdigit():
                number = True
            elif password[i] in symbols:
                sym = True
            i+=1

        if (upper and lower and number and sym):
            print("Valid Password")
            break
        