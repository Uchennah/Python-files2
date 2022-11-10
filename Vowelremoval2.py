#Removing Vowels from a word/string of words using a function

def removeVowels(string,Newstring): #The 'def' function does what the code in Vowelremoval1 does.
    vowels = ('a','e','i','o','u')
    for c in string.lower():
        if c in vowels:
            Newstring = Newstring.replace(c,'')
    return (Newstring)
print('Enter X to exit program')
string = input('Enter a word or string of words: ')
if string == 'X':
    exit()
else:
    Newstring = string
    print('Removing vowels from word(s).....')
    Newstring = removeVowels(string,Newstring)
    print('New word(s) after vowel removal is: ' +Newstring)

#same code but with the use of a 'def' function to define what we want the code the perform, then we are able to call that defined function anywhere with the code.
