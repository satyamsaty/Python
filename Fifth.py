student = {'name':'satyam','address':'subhash nagar','subjects':'[english],[hindi]'}
print(student)
print (student['name'])
print (student['subjects'])
#print (student['phone']) #key error
#using get()  method

print(student.get('phone')) #we will get none , not key error
print(student.get('phone','not found'))#want to add not found
student['phone']='5555=5555555'
print(student.get('phone'))
student['name']='shivam'
print(student.get('name')) #overrride name
#use update() method to update all at once

student.update({'name':'sundram','address':'bangalore'})
print (student)
#use del() method to delete but it will not return anything .use pop() to return .

del student['address']
print(student)
phone=student.pop('phone')
print(student)
print (phone)
print(len(student))
print (student.values())
print (student.keys())
print (student.items()) #to print both key and values

#using loops

for key,value in student.items():
    print(key,value)














