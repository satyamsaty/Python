greeting = 'hello'
name = 'Michael'
message = greeting + name
print (message)
message = '{}, {}. Welcome!'.format(greeting,name)
print (message)
message = f'{greeting}, {name.upper()}. welcome!'
print (message)
print (dir(name))
print (help(str))