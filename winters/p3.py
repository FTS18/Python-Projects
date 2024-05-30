'''Write a Python program that creates a binary file to store student information, including names, classes, 
and roll numbers. Additionally, the program should be capable of displaying all the records inserted into 
the file. Create the following functions to perform these operations: [8]
a. storeData(): To store student information
b. showData(): To show details of all the students'''
import pickle
def storeData():
    with open("xyz.pkl",'a') as f:
        n=int(input("No. of students: "))
        
    
def showData():
    