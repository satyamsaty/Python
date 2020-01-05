class Employee:
    raise_amount=1.5

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def payraise(self):#using instance variables for pay ,suppose for all employee they are giving same increment,so better to use class variable
        self.pay=int(self.pay*self.raise_amount)
e1= Employee('satyam','kumar',50000 )
print(e1.email)

print(e1.fullname())
print(e1.pay)
e1.payraise()
print(e1.pay)
##################
print(e1.raise_amount)
#########################
print(Employee.raise_amount)
print(e1.__dict__) #to check namespace ,raise amount will not be here
##################
print(Employee.__dict__) #since raise amount is  class variable ,raise amount will be listed {'__module__': '__main__', 'raise_amount': 1.5,

#e1.raise_amount=200
##########verifying the above

#print(e1.raise_amount)
#print(Employee.raise_amount)
##################################################

Employee.raise_amount=400
print(e1.raise_amount)
print(Employee.raise_amount)







