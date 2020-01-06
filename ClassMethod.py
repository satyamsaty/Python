class Employee:

    raise_amount=1
    num_of_emps=0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

        Employee.num_of_emps += 1
    def fullname(self):
        return'{}{}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
         cls.raise_amount = amount


emp_1=Employee('satyam','kumar',50000)
emp_2=Employee('shivam','kumar',70000)
print(emp_1) #<__main__.Employee object at 0x000002B2D4488460>
print(emp_1.pay) #50000
print(emp_2.first)
print(emp_1.fullname())
print(Employee.raise_amount)
print(Employee.num_of_emps)
Employee.set_raise_amount(4)
print(Employee.raise_amount)


