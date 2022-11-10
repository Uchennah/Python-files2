import os

Directory = input('Enter the Directory(Use \\\ to seperate the directories): ')
Directory = Directory.strip('\n')
os.chdir(Directory)

filename = input('Enter the name of the file: ')
content_of_file = 'Dear Sharon,\nI hope this mail meets you well\n I am writing to schedule a meeting for 12pm WAT Lagos time tomorrow. If this works for you please revert\n Thanks and Best Regards'
file_name= open(filename, 'wt')
file_name.write(content_of_file)
file_name.close()
