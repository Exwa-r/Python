#PigLatin - From the input string, for each word, remove the first chars until a vowel, 
#add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputSentence = input("Enter your String : ").lower()
result = ""

pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']
# nonVowels = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

for word in inputSentence.split(): #gets the word in a sentence
    #take the first chars until a vowel
    i=0
    while i < len(word):
        if word[i] in vowels:
            result += word[i:].capitalize() + word[:i] + pigLatinKey + " "
            break
        # elif word[i] in nonVowels:
        #     pass
        i+=1

print(result)

