import secrets
import string
import pyperclip
from datetime import datetime
import csv

def genp(len=12):
    if len < 1:
        raise ValueError("Password length must be at least 1")
    chars = string.ascii_letters + string.digits + string.punctuation
    passwd = ''
    for _ in range(len):
        passwd += secrets.choice(chars)
    return passwd

def customp():
    exclude = input("Characters to exclude (leave blank if none): ")
    include = input("Characters to include (leave blank if none): ")
    
    if not include:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        chars = include

    fchar = ''
    for c in chars:
        if c not in exclude:
            fchar += c

    len = int(input("Enter the desired length of the password: "))
    passwd = ''
    for _ in range(len):
        passwd += secrets.choice(fchar)
    return passwd

def savep(passwd):
    with open("passwords.csv", "a", newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date, time = timestamp.split()
        writer.writerow([date, time, passwd])

def copyc(passwd):
    pyperclip.copy(passwd)
    print("Password copied to clipboard.")

def menu():
    print("Random Password Generator")
    print("1. Generate a random password")
    print("2. Enter a custom password")
    choice = input("Choose an option (1 or 2): ")
    
    if choice == '1':
        try:
            len = int(input("Enter the desired length of the password: "))
            passwd = genp(len)
            print("Generated Password:", passwd)
            savep(passwd)
            copyc(passwd)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '2':
        passwd = customp()
        print("Custom Password:", passwd)
        savep(passwd)
        copyc(passwd)
    else:
        print("Invalid choice. Please choose 1 or 2.")

menu()
