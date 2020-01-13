import sys
sys.path.append('/Users\satykumar\Desktop/My-Modules')#better way to add env file in path in windows

#importing other
import time
import calendar
import math
import random
import os
courses=['history','math','physics','datascience']

random_course=random.choice(courses)
print (random_course)
today=time.date.today()
print(today)

print(os.getcwd())

print(os.__file__)  // to see standard library for os module

leap_year=calendar.isleap(2020)
print (leap_year)
rads=math.radians(90)
print(math.sin(rads))
#import import3 as mm
#from import3 import find_index
from import3 import find_index,test




#index= import3.find_index(courses,'math')
#print (index)

#index= mm.find_index(courses,'math')
#print (index)

index=find_index(courses,'datascience')
print(index)
print (test)
print(sys.path)
