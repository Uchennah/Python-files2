password = "Uchenna5044"

while True:
    uchennaone = input('Enter your name:')
    uchennatwo = input ('Enter your email address:')
    uchennathree = input ('Enter password:')
    uchennathree = str(uchennathree)

    if uchennathree ==  password:
        print("Correct Password")
        break

    else:
        print("Wrong Password")
        print("Re-enter your details")

        continue
        

uchennafour = input ('Enter year of Admission:')
uchennafive = input('Enter year of Graduation:')
uchennafour = int(uchennafour)
uchennafive = int(uchennafive)

print('Calculating Years spent in school.....')
Years_spent_in_school = uchennafive - uchennafour
print('Years_spent_in_school is: ' + str(Years_spent_in_school))


    
   


    


    



