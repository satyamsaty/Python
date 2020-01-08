import os
print(os.getcwd())
#f=open('testfile.txt') since testfile.txt is not present , we got FileNotFoundError: [Errno 2] No such file or directory
#1 way
#try:
#    f=open('testfile.txt')
#except Exception:
#    print('Sorry .This file doenot exist')
#better way to fix errors in 2nd way
#try:
 #   f=open('testfile.txt')
 #   b=var#name error
#except Exception:
#    print('sorry, i will not be able to give anything related to var ')
#2 way

#f=open('testfile.txt')#FileNotFoundError: [Errno 2]
#var=b#name error
try:
    f=open('testfile.txt')
    var=b
except FileNotFoundError:
    print('file not found error')
except Exception :#will go here if f=open('test_file.txt') is correct
    print('sorry!something went wrong')

##################333
try:
    f=open('testfile.txt')
   # var=b
except FileNotFoundError as e:
    print(e)#[Errno 2] No such file or directory: 'testfile.txt'
except Exception as e :#will go here if f=open('test_file.txt') is correct
    print(e)#name 'b' is not defined
else:
    print(f.read())
    f.close()
finally:#it will always execute , if try is true , it will go to else and execute the block and if false it will execute except block
    print('i will always execute no matter what')

#how to create our own exception
try:
    f=open('corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception#using raise we created one exception called Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('errorrrr')
else:
    print(f.read())
    f.close()
finally:
    print('i will always execute')





