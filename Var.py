#variablescope
#LEGB local , enclosing , global , builtins
import builtins #to import builtin fxns
#print(dir(builtins)) #builtin list using dir
x='global x'#global variable

#def test():
 #   y = 'local y' #local to test fxn
    #global x #if we want to change value of global x , means to override,, it is not used much .
  #  x='local x'
 #   print(y)
  #  print(x)#global variable 1stlocal then enclosing then global

#test()
#print(y)#name 'y' is not defined
#print(x)#executed as it is global

#def test1(z):#local z
#    print(z)

#test1('local z')

#def min():#TypeError: min() takes 0 positional arguments but 1 was given
#  pass
#def min_m():
    #pass
#m=min([1,2,3,4,5]) #min is builtin fxns
#print (m)

def outer():
    x= 'outer x'##enclosing

    def inner():
        nonlocal x ##affecting x variable of the outer funtion
        x='inner x'
        print (x)

    inner()
    print(x)

outer()
print(x) ##global x

##see decorators for more info for non local




