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