'''Write a Python program that includes two functions: storeData() and countNT(). These functions are designed
to manage user details in a Text file named lesson.txt. [8] a. storeUser(): i. This function prompts the user 
to input some data. ii. It then stores that data in lesson.txt. b. checkUser(): i. This function reads the data
from lesson.txt. ii. After fetching data, counts the occurrence of ‘A’, ‘a’, ‘n’ and ‘N’ letters in the file.'''

f=open("lesson.txt","a")
def storeData():
    x=input("Enter something: ")
    f.write(x)
    f.close()
def countNT():
    f=open("lesson.txt","r")
    c=f.read()
    n=a=0
    for i in c.lower():
        if i=="a":
            a+=1
        if i=="n":
            n+=1
    print("No. of A: ",a)
    print("No. of N: ",n)
storeData()
countNT()