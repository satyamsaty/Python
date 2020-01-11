import csv
import os
print(os.getcwd())

#with open('names.csv','r') as csv_file:
 #   csv_reader=csv.reader(csv_file)#reader method to read csv file

  #  next(csv_reader)#to remove 1st row
   # for line in csv_reader:
    #    print (line[2])#to print only second column
    #print(csv_reader)

#with open('names.csv','r') as csv_file:
 #   csv_reader=csv.reader(csv_file)


  #  with open('new_names.csv','w') as new_file:
   #     csv_writer=csv.writer(new_file,delimeter='\t')
    #    for line in csv_reader:
     #       csv_writer.writerow(line)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)








