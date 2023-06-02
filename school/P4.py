#Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.
import json
y=["yes","y","ye","yee","yed","yew","ya","yup"]
def printName(n):
    if n in records.keys():
        name=records[n]
        print("Name: ",name)
    else:
        print("ERROR: Roll Number not found! \nDo you want to create a new entry?", end=": ")
        x=input("").lower()
        if x in y:
            inp=input("Enter name: ")
            records[str(c)]=inp
file=open("data.txt", "r")
records=json.load(file)
f=len(records)-1
c=int(list(records.keys())[f])+1
rno=input("Enter the roll number: ")
printName(rno)
with open("data.txt", "w") as file:
    json.dump(records, file, indent=4, sort_keys=True)