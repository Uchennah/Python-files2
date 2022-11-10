#Use of dictionary to print Exam Scores

ExamScores = {'David':'A', 'Mark':'B', 'Razus':'E', 'Joseph':'A','Juwon':'F','Uzondu':'D'}
print('Enter name of candidate to see Exam Score ')
Candidate= input('Enter Candidate Name: ')
if Candidate == None:
    exit()
if Candidate in ExamScores:
    print('Exam Score is : '+ ExamScores[Candidate])
else:
    print('Invalid Name.... Try Again!')
