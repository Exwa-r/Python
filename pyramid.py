#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

myName = input("Enter your String : ").upper()
pyramid = '' #Empty String

for i in range (len(myName)):
     
    print(myName[0:i+1])