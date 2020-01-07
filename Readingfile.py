import os
print(os.getcwd())
print(os.listdir())

#FileObjects and reading files

f = open('test.txt.txt','r') # r for read , w for write, open() to open a file , in current directory , we can use path to refer os.cwd()
print(f.mode)
print(f.name)
f.close() #dont forget to close file
#context manager no need to close manually
#with open('test.txt.txt','r') as f: #with keyword ,f is variable name
 #   print(f.name)
#print(f.closed) #returns true if file is closed
#          pass
#print(f.read())#ValueError: I/O operation on closed file.
#with open('test.txt.txt','r') as f:
    #f_contents=f.read()
    #print(f_contents) #for small file it is okay to read , no memory issue
   # f_contents=f.readlines()
   # print(f_contents) #['1) This is a test file\n', '2) With multiple lines of data...\n',
    #f_contents=f.readline() #one line at at time
    #print(f_contents)
    #f_contents = f.readline()  # there is one new line as well .one line at at time ,  so 2nd line printed
    #print(f_contents)
    #f_contents = f.readline()  # one line at at time
    #print(f_contents,end='')
    #f_contents = f.readline()  # one line at at time
    #print(f_contents,end='') #no new line for b/w 3rd and 4th , in this case if large file , we can run out of memory
    #use for loop
    #print(f.read())
  #  for line in f:
  #      print(line,end='')#f.read() returns all lines,not reading all lines at once so no memory issue
        #print('test')
#if we want to limit per number of character
    #f_contents=f.read(100)#say 100 characters
    #print(f_contents,end='')
    #f_contents = f.read(100)  # say 100 characters
    #print(f_contents, end='')
    #f_contents = f.read(100)  # say 100 characters #all characters read ,returned empty string
    #print(f_contents, end='')
 #   size_to_read=10
 #   f_contents=f.read(size_to_read)
 #   print(f_contents,end='')
    #print(f.tell()) #tells us where we are
   # while len(f_contents) >0:
    #    print(f_contents,end='')#infinite loop , print * if end ='*'
     #   f_contents=f.read(size_to_read)
    #f.seek() to change the location to say 0
  #  f.seek(0)
  #  f_contents = f.read(size_to_read)
  #  print(f_contents)#1) This is1) This is

    ####writing to files , if it is in read mode and we want to write to file it is not possible
with open('test2.txt','w') as f:
        #pass #it will create test2 in current location , also w will overwrite if test2.txt already present , we can use a for it , a will ammend
        f.write('TEST')#it will write TEST to test2.txt
        f.seek(0)#it will replace only T with t , so tEST
        f.write('t')
with open('test.txt.txt','r')as rf:
    with open('test.txt.copy.txt','w') as wf:
        for line in rf:
            wf.write(line) #to copy lines from one file to another file
#for pictures , we use binary mode    , so for r we use rb and for w we use wb

with open("bronx.jpg.PNG", "rb") as rf:
   with open("bronx_copy.jpg", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)




















