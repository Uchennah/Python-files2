class Student:
    stuCount = 0

    def __init__(self,Firstname,Lastname,Subject,Grade):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Subject = Subject
        self.Grade = Grade
        Student.stuCount += 1
        

    def displayStudentCount(self):         #This part of this code is not compulsory. Can be removed and the code would still run well
        print('Total number of Students is %d' % (Student.stuCount)) 

    def StudentInformation(self):
        print('First Name: ' + self.Firstname + '\n' + 'Last Name: ' + self.Lastname + '\n' + 'Subject: ' + self.Subject + '\n' + 'Grade: ' + self.Grade)

print('Usage... \nQuit -- End Program \nAdd -- Add New Student Details \nDisplay -- Display the last Students Information \nTotal -- Total number of Students')
while True:
    option = input('Enter an Option: ')
    if option == 'Quit':
        break
    elif option == 'Add':
        first_name = input('Enter First Name: ')
        last_name = input('Enter Last Name: ')
        subject = input('Enter the Subject: ')
        grade = input('Enter the Grade: ')
        student = Student(first_name,last_name,subject,grade)
    elif option == 'Display':
        student.StudentInformation()
    elif option == 'Total':
        print('Total number of Students is %d' % (Student.stuCount))
        
    else:
        print('Option does not exist.. Pick an option from: \nQuit \nAdd \nDisplay \nTotal')
    
