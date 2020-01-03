import os
from datetime import datetime

print(os.getcwd()) #get current working directory
os.chdir('C:/Users/satykumar/PycharmProjects') #change directory
print(os.chdir('C:/Users/satykumar/PycharmProjects'))
print(os.getcwd())
os.chdir('C:/Users/satykumar/PycharmProjects/Python')
print(os.getcwd())
print(os.listdir()) # to check files in directory
#os.mkdir('test5')#subdirectory not allowed
#os.makedirs('test3/test4')
print(os.listdir())
#os.rmdir('test1') #remove directory
#os.rmdir('test2')
#os.removedirs('test3/')
os.rename('FIRST.py','first.py') #to rename
print(os.stat('first.py').st_size)
print(os.stat('first.py').st_mtime)
rad=os.stat('first.py').st_mtime
print(datetime.fromtimestamp(rad)) #modified time in IST

for dirpath,dirnames,filenames in os.walk('C:/Users/satykumar/PycharmProjects/Python'): #to check files within directories
    print('dirpath',dirpath)
    print('dirnames',dirnames)
    print('filenames',filenames)

print(os.environ.get('USERPROFILE')) #homedir

file_path=os.path.join(os.environ.get('USERPROFILE'),'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt')) #whether file exists or not

print(dir(os.path)) #to check what all are present for os.path
#print (os.getcwd())
#print(os.listdir())
#print(dir(os))