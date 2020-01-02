def funct1 ():
    pass

print (funct1)
print (funct1())
def funct2 ():
    print ('1st function')

funct2()
funct2()
funct2()
funct2()

def funct3 ():
    return 'second_function'

print (len('satyam'))

print(funct3().upper())

#using parameters with format() method

def func3 (greetings):
    return '{} Satyam.'.format(greetings)

print(func3('hi'))

def func4(greeting,name):
    return '{} {}'.format(greeting,name)
print(func4('hi','shivam'))


def student_info(*wargs, **kwargs):
    print (wargs)
    print (kwargs)

student_info('math','chemistry',name='satyam',age=26)

#it will come in one line
def student_infos(*args,**kwargs):
    print(args)
    print(kwargs)

courses=['math','art']
info={'name':'john','age':22}

student_infos(courses,info)

#correct way

def student_infos(*args,**kwargs):
    print(args)
    print(kwargs)

courses=['math','art']
info={'name':'john','age':22}

student_infos(*courses,**info)

