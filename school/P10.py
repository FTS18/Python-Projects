import pickle
import os

def inp():
    uname = input("NAME: ")
    uid = input("ID: ")
    ucity = input("CITY: ")
    return {"name": uname, "id": uid, "city": ucity}

def addUser(user, users):
    for existing_user in users:
        if user["id"] == existing_user["id"]:
            print("User already exists!")
            return
    users.append(user)
    with open("users.txt", "wb") as file:
        pickle.dump(users, file)
    print("User added successfully.")

def removeUser(uid, users):
    for user in users:
        if user["id"] == uid:
            users.remove(user)
            with open("users.txt", "wb") as file:
                pickle.dump(users, file)
            print(f"User with ID {uid} removed.")
            return
    print(f"User with ID {uid} not found.")

def displayUser(uid,users):
    for user in users:
        if user["id"] == uid:
            print("NAME:",user["name"],"\nID:", user["id"],"\nCITY:", user["city"])
            return
    print(f"User with ID {uid} not found.")

def main():
    if os.path.exists("users.txt"):
        with open("users.txt", "rb") as file:
            users = pickle.load(file)
    else:
        users = []
    inpf=input("What do you want to perform:\n1) Add User (a)\n2) Remove User (r)\n3) Display User (d)\n>>")
    if inpf=="a":
        user = inp()
        addUser(user, users)
    elif inpf=="r":
        ruid = input("ID of the user you want to remove: ")
        removeUser(ruid, users)
    elif inpf=="d":
        n=input("Enter ID of user to display: ")
        displayUser(n,users)
    else:
        return 

if __name__ == "__main__":
    main()
