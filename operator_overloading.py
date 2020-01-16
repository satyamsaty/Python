class Employee:
    def __init__(self,first,last,pay):##__ is douunder
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last +'@test.com'
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first,self.last,self.pay)
    def __str__(self):
        return '{} - {}'.format(self.full_name(),self.email)
   # def __add__(self,other):
    #    return self.pay + other.pay



emp_1=Employee('satyam','kumar',70000)
emp_2=Employee('shivam','kumar',90000)
print( emp_1 + emp_2 )   #due to __add__ it passed if removed unsupported operand type(s) for +: 'Employee' and 'Employee'
print(emp_1.__repr__()) #<__main__.Employee object at 0x0000023C9B088460>satyam, kumar, 70000
print(emp_1)#satyam, kumar, 70000##if __str__ is commented
print(emp_1)#satyam kumar - satyam.kumar@test.com
print(emp_1.__repr__())
print(emp_1.__str__())
print(repr(emp_1))
print(str(emp_1))
##__init__,__repr__,__str__ most used

print(int.__add__(2,3))
print(str.__add__('a','b'))

###pending practice

