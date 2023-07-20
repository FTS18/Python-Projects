#Create a binary file with roll number, name and marks. Input a roll number and update the marks
import json
file = open('marks.txt', 'r')
records=json.load(file)
from random import *
while True:
    y=["yes","y","ye","yee","yed","yew","ya","yup"]
    try:
        print("")
        inp=int(input("Enter Roll Number: "))-1
        marks=int(input("Enter Marks: "))
        records[inp][2]=marks
        print(records[inp])
        with open("marks.txt", "w") as file:
            json.dump(records, file, sort_keys=True)
    except IndexError:
        print("Roll number not found in the database!")
    except ValueError:
        print("Invalid credentials provided!")
    x=input("Restart?: ")
    if x in y:
        continue
    else:
        break