largest = None
smallest = None

while True :
    num = raw_input("Enter a number: ")
    if num == "done" :
        break
    try :
        num = int(num)
    except :
        print ("Invalid input")
        continue
    if largest is None :
        largest = num
    elif largest < num :
        largest = num
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = num

print ("Maximum is", largest)
print ("Minimum is", smallest)
