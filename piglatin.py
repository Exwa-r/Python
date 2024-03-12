#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = input("Enter a Sentence : ")
result=""
pigLatinKey = 'ay'
for word in inputSentence.split(): #gets the word in a sentence
    #take the first char
    firstChar = word[0] #to take the starting element
    word = word[1:] + firstChar + pigLatinKey
    result+=word + ' ' #adding the words with a space to seperate


print(result)