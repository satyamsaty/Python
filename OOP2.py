class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp1=Employee('satyam','kumar',50000)
emp2=Employee('shivam','kumar',70000)
print(emp1.email)
print(emp2.last)
print(emp1.fullname()) #here self will solve the purpose 
#print(emp.fullname)#it willnot work
print(Employee.fullname(emp1)) #if we are using class , we need to pass instance as well .
print('{}{}'.format(emp2.first,emp2.last)) #without functions