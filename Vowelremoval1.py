#Removing Vowels from a word/string of words

print('Enter X to exit code') #User is prompted to enter X if he/she wants to exit the code
string = input('Enter a word or string of words in lowercase: ') #User is prompted to enter a desired word or string of words
if string == 'X': #if user enters X instead of a word, the program..
    exit() #.. is prompted to stop running and exit
else: #If the user doesn't enter X, then the program does the following..
    NewString = string #Here we define a new variable as our previous variable(string) is already defined
    print('Removing vowels from word(s).....') #here a prompt shows the user what's going to happen after keying a word/ string of words
    vowels =('a','e','i','o','u') #here the vowels are defined
    for c in string.lower(): #Here we check for each 'c' (character) in the word or string of words entered. '.lower' function here causes the program to remove only vowels in lowercase 
        if c in vowels: #here we check for each charcter in the words or word entered if they are vowels...
            NewString = NewString.replace(c,'') #.... if there are vowels, the '.replace' function we've used, replaces that character with an empty space which is depicted with ()
    print('New word after vowel(s) removal is: '+NewString) #Once the check is performed, we print the new word after vowels are removed,














