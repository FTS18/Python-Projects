'''Consider a scenario where you have a list of products and their corresponding prices stored in a list. 
Write a program with separate user-defined functions to perform the following operations: [8] a. createList:
Use this function to insert data in list in the given format. For example: productPrices = [[‘Laptop’,10],
[‘Smartphone’,12],[‘Camera’,8]] b. storeCSV: Use the list created by the createList function and store 
that data in a csv file named electronics.csv.'''
import csv
def createList():
    productPrices=[]
    n=int(input("Enter no of products: "))
    for i in range(n):
        pname=input("Enter Product Name: ")
        price=input("Enter Price: ")
        l=[pname,price]
        productPrices.append(l)
    return productPrices
g=createList()
def storeCSV():
    f=open("elecronics.csv",'w',newline="")
    x=csv.writer(f)
    x.writerows(g)
storeCSV()
print(g)