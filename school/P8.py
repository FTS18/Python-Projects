#Create a CSV file by entering user-id and password, read and search the password for given user-id
import csv
id=input("USER ID: ")
with open('admin.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for i in reader:
        if id in i:
            print("PASSWORD: ",i[2])
            break
    else:
        print("User not found!")