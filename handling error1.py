import os
os.chdir('C:\\Users\\Stephnie\\Desktop')

try:
    fn = open('Afile.txt', 'a')
    fn.write('What a crazy and vile world')
    fn.close()
except:
    print('File does not exist')
else:
    print('Opening file....')
