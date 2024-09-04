# String manipulation exercises. Use builtin functions as needed.

# 1. Print the level of the password security and if the password is acceptable
#     Weak - only alphabets or only numbers or only special chars
#     Ok - at least one alphabet, one number and one special char  
#     strong - at least three alphabets, two numbers and one special char  
#     Very strong - same as strong, but at least 16 count

#     All passwords must be at least 8 chars long. You can use RegEx if you want.
alphabet=""
symbol=""
password=input("Enter your password :")
number=""
alpha="abcdefghijklmnopqrstuvwxyz"
num=["1","2","3","4","5","6","7","8","9","0"]
char="!@#$%^&*()?"
if(len(password)>=8):
        for i in (password):
            if(i in num ):
                number+=i                                                                       #aa22
            else:
                continue
           
        for i in password:
            if(i in alpha):
                alphabet+=i  
            else:
                continue
        for i in password:
            if(i in char):
                symbol+=i
            else:
                continue
               

        if(len(number)==len(password) or len(alphabet)==len(password) or len(symbol)==len(password)):
            print("Weak password")        
        elif (len(number)<2 and len(alphabet)<3 and len(symbol)<2):
            print("OK")
        elif(len(number)>=2 and len(alphabet)>=3 and len(symbol)>=1 and len(password)>=16):
            print("very strong")
        elif(len(number)>=2 and len(alphabet)>=3 and len(symbol)>=1):
            print("Strong Password")    
        else:
            print("Your password should in alphabet and number and symbol")
else:
    print("enter a valid password with atleast 8 char long")