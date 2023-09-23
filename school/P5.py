#Create a binary file with roll number, name and marks. Input a roll number and update the marks
import pickle
l=[["1", "Ananay", 52], ["2", "Aditya", 69], ["3", "Arunjay", 45], ["4", "Dishank", 56], ["5", "Ishan", 67], ["6", "Vansh", 61]]
file = open('marks.pkl', 'wb')
pickle.dump(l,file)
file.close()

f = open('marks.pkl', 'rb+')
records=pickle.load(f)
print("")
inp=int(input("Enter Roll Number: "))-1
marks=int(input("Enter Marks: "))
records[inp][2]=marks
print(records[inp])
print(records)
pickle.dump(records, f)
