Name = input('Enter Name:')
Email = input ('Enter Email Address:')
Year_of_Birth = input ('Enter Year of Birth:')
Current_Year = input('Enter Current Year')
Admission_Year = input('Enter Admission Year:')
Graduation_Year = input('Enter Graduation Year:')

Name = str(Name)
Email = str(Email)
Year_of_Birth = int(Year_of_Birth)
Current_Year = int(Current_Year)
Admission_Year =int(Admission_Year)
Graduation_Year = int(Graduation_Year)

print("Calculating Age.....")
Age = Current_Year - Year_of_Birth 
print("Age is: " + str(Age))

print("Years Spent in School....")
Years_Spent_in_School = Graduation_Year - Admission_Year
print("Years Spentin School: " + str(Years_Spent_in_School))



   
    


