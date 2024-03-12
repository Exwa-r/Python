# ########## Program 4
# #PigLatin - From the input string, for each word, remove the first chars until a vowel, add it to the end of the word
# #and add 'ay' to it.
# #eg I am Python
# #answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputSentence = input("Enter a String : ")
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']

for word in inputSentence.split(): #gets the word in a sentence
    
     #take the first chars until a vowel
     first_vowel_index = 0
     #FillinMissingCode - check if the word has more than one char
     for index, char in enumerate(word): #returns both the index and the char in the word
         if char in vowels:
             first_vowel_index=index
             break
            
          #FillinMissingCode - check if the char is vowel or not


 
     word = word[first_vowel_index+1:] + word[0:first_vowel_index] + pigLatinKey
     print(word)


word="Python"
# word=word[5:]+word[0:5]+pigLatinKey
#print(word)
print(word[2:5])