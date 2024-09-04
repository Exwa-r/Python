s = "Hello world this is a string"
reverse = ""
array_string = s.split()

for i in range(len(array_string)):
    reverse = array_string[i] + " " + reverse 
print(reverse)