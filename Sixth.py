#no switch and case statements in python
language='python'
if language=='python':
    print('languae is python')
elif language=='java':
    print('language is java')

else:
    print('no match')

#use of or and and not
user='admin'
logged_in=False
#logged_in=False
#if user=='admin' or logged_in:
#    print('user is logged in')
#else:
#    print('not logged in')

if not logged_in:
    print ('logged in')
#use is id(a) == id(b)

a=[1 , 2 , 3, 4]
b=[1, 2, 3, 4]

if a == b:
    print (" a == b")
c=b
print(id(b))
print(id(c))

if b is c:
    print ('b is c')#same memory allocation

#what all defaults to false

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition= ()

if condition:
    print ('go to if block means true')
else:
    print('go to false block')


condition= []

if condition:
    print ('go to if block means true')
else:
    print('go to false block')
condition= {}

if condition:
    print ('go to if block means true')
else:
    print('go to false block')
condition= None

if condition:
    print ('go to if block means true')
else:
    print('go to false block')

