# Check if the username and password is correct. 
# Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
# passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
# name of the company mentioned in the username, followed by any 3 numbers.
# eg username : myname@sayur.com. password - mnamesay123

username=input("Enter Your Username : ").lower()
after_at=""
name=''
company=''
at_=0
dot_ =0
num_ =0
number=['1','2','3','4','5','6','7','8','9','0']

a=['.com','.edu','.tech','.org']

# if username[-4:] in a: #whether it contains [.com .org .edu .tech]
    
for char in username:  #for loop to check the username contains only one "@" char
    if char == "@":
        at_ += 1

for i,char in enumerate(username):  #to split the company name after "@"
    if at_ == 1:
        if char == "@":
            name = username[0:i]  #storing the part Before "@"  to store name  
            after_at = username[i+1:]  #storing the part after "@" to find company name
            for dot in after_at:   #used for checking number of "." in the username
                if dot == ".":
                    dot_ += 1
    else:
        flag = False

for i,char in enumerate(after_at):   #gmail.com
    if dot_ == 1:
        if char == ".":
            company = after_at[:i]  #storing company name
            if after_at[i:] in a:   #Meera@gmail.com
                flag = True
    else:
        flag = False


if flag == True:
                   
    password=input("Enter Your Password : ")

    if (password[0] == name[0]) and (password[1] == name[2] and (password[2:5] == name[-3:]) and (password[5:8] == company[0:3])):
        for i in password[8:]:
            if i in number:
                num_ += 1
        if num_ == 3:
            flag = True
        else: 
            flag = False

    if flag == True:
        print("Your User-Name and Password are Perfect..!! ")
    else:
        print("Your User-Name and Password are Incorrect..!! ")

elif flag == False:
    print("Your User-Name is Incorrect..!! ")