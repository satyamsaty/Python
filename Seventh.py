subjects= ['eng','hindi','maths']
for item in subjects:
     print (item)

nums= [1, 2, 3, 4 ,5 ]
for num in nums:
    for item in 'abc':
     print (num,item)


nums2= [1, 2, 3, 4, 5]
for num2 in nums2:
    if num2 == 4:
        print('found it !')
        break
    print (num2)#indentation should be proper

nums3= [1, 2, 3, 4, 5]
for num3 in nums3:
    if num3 == 4:
        print('escape it!')
        continue
    print (num3)#indentation should be proper and 5 will print here .

#using range

for i in range(10):
    print (i)
for i in range(1,11): #if we want to start with 1
    print (i)

x = 0
while x <10:
    if x ==9:
        print ('found it!')
        break
    print(x)
    x+= 1