#Check if the username and password is correct. 
#Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
#passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
#name of the company mentioned in the username, followed by any 3 numbers.
#eg username : myname@sayur.com. password - mnamesay123

username=input("Enter your UserName to Check : ")
length=len(username)


if (" " not in username):
    if ("@gmail.com" in username[-11:]):
        if ("@" not in username[:-11]):
            if (".com" not in username[:-5]):
                print("Valid")
        else:
            print("InValid")
    else:
        print("InValid")
else:
    print("Invalid")