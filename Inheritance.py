class Employee:

    raise_amount=0.5
    def __init__(self,first,last,pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email=first + '.' +  last + '@test.com'

    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)


class Developer(Employee): #Inheriting Employee class
    raise_amount=1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)##to call Employee init method
        self.prog_lang=prog_lang

#print(help(Developer))#to check what is inherited
dev_1=Developer('Shivam','kumar',70000,'java')
dev_2=Developer('saty','kumar',80000,'python')
dev_3=Developer('shiv','kumar',90000,'javascript')
#print(dev_1.first)
#print(dev_2.prog_lang)
#print(dev_1.first)#it inherited from employee class
#print(dev_1.full_name())
#print(dev_2.prog_lang)
#emp_1=Employee('satyam','kumar',50000)
#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)
#print(dev_1.pay)
#dev_1.apply_raise()#doenot impact Employee class
#print(dev_1.pay)

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees= []
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
         self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.full_name())



man_1=Manager('sundram','kumar',80000,[dev_1])

print(man_1.email)
#man_1.print_emps()
man_1.add_emp(dev_1)
#print(man_1.print_emps())
#print(man_1.first)
man_1.add_emp(dev_3)

man_1.remove_emp(dev_2)
print(man_1.print_emps())

print(isinstance(man_1,Manager))#to check if man_1 is instance of Manager
print(isinstance(man_1,Employee))#true
print(isinstance(man_1,Developer))#false
print(issubclass(Developer,Employee))#to check if Developer is subclass of Employee
print(issubclass(Developer,Manager))#False


##realcase httpexception




#emp_1=Employee('satyam','kumar',50000)
#print(emp_1.first)
#print(emp_1.email)
#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)
#print(emp_1.full_name())

