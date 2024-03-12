#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g


inputString = input("Enter Your Syring : ").replace(" ","")
i = 0 #counter to track the chars
newString = "" #empty string
while i < len(inputString):
    newString += inputString[i:i+2] #to take 2 elements from the list
    newString += " " #add space
    i+=2
#check to add the chars at the end

print (newString)