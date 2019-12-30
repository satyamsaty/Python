courses = ['english','hindi','maths','science']
for index,item in enumerate(courses , start=1):
      print (index,item)
#courses to convert
course_str = ', '.join(courses)
print (course_str)
new_list = course_str.split(',') #converting string to lists
print (new_list)
course_str1 ='- '.join(courses)
print (course_str1)
courses_2 = ['history', 'geogoraphy']
print (courses_2.index('history')) #to check index
print ('history'in courses_2)
print ('cse' in courses_2)
nums = [1, 5, 2, 4, 3]
print (min(nums))
print (sum(nums))
print (courses[0])
print (courses[-1])
#print (courses[4])
print (courses[0:2])
print (courses[2:])
print (courses[0:])
print (len(courses))
courses.append('art')
print(courses)
courses.insert(0,'computer')
print (courses)
#courses.insert(0,courses_2)
#print (courses)
#print (courses[0])
courses.extend(courses_2)
print (courses)
courses.remove('english')
print (courses)
popped=courses.pop()
print(popped)
print (courses)
courses.reverse()
print (courses)
courses.sort()
sorted_courses=sorted(courses)
print(sorted_courses)
print (courses) #alphabetical order
courses.sort (reverse=True)
print (courses)
#mutable and immutable
list_1= ['abc','def','ghi','jkl']
list_2= list_1
print (list_1)
print (list_2)
list_1[0]='mno'
print (list_1) #mutable
print (list_2)

#Tuples

tuple_1= ('abc','def','ghi','jkl')
tuple_2= tuple_1
print (tuple_1)#'tuple' object does not support item assignment
print (tuple_2)
#tuple_1[0]= 'mno' #'tuple' object does not support item assignment
#print (tuple1)
#print (tuple2)'tuple' object does not support item assignment

#sets

sets_1 = {'english', 'hindi', 'maths'} #unordered sets
print(sets_1)

sets_2 = {'english','hindi','maths','english'} #dont support duplicates'tuple' object does not support item assignment
sets_3 = {'cse','hindi','networking'}
print(sets_2.intersection(sets_3))
print(sets_2.difference(sets_3))
print(sets_2.union(sets_3))
empty_list = list()
print(empty_list)
empty_tupple= tuple()
print(empty_tupple)
empty_set= set()
print(empty_set)





