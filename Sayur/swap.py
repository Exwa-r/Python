#Write a program that will swap two numbers. 



num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))

print("Before Swapping")
print(f"[{num1},{num2}]")

#temp=0 num1=1 num2=2
temp=num1  #temp=1 num1=1 num2=2
num1=num2  #temp=1 num1=2 num2=2
num2=temp  #temp=1 num1=2 num2=1

print("After Swapping")
print(f"[{num1},{num2}]")



