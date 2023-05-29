'''• addUser() function will add a new user in the list. User information will be in a dictionary format having name, id and city. E.g., L = [{‘name’:"Virath Kohli", "id":"18", "city":"Delhi" }, {‘name’:"Rohit Sharma", "id":"45", "city":"Nagpur" }]. 

• removeUser() function will accept id as an argument and will delete the user if id exists in the list.

• displayUser() function will accept id as an argument and will display the user if id exists in the list, if no id is passed it will print the list of all users'''
import json
file=open("users.txt", "r+")
users=json.load(file)

def inp():
    name=input("NAME: ")
    id=input("ID: ")
    city=input("CITY: ")
    global user 
    user={"name":name, "id":id, "city":city }

def addUser():
    inp()
    if user in users:
        print("User already exists! ")
    else:
        users.append(user)
        with open("users.txt", "w") as file:
            json.dump(users, file, indent=4)
def removeUser(id):
    print(users[id])