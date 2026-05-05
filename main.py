import random
import json
import os
from getpass import getpass

FILE = "passwords.json"

def loadData():
    if not os.path.exists(FILE):
        return {}
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}

def saveData(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def generatePassword(length):
    
    possibleLower = 'qwertyuiopasdfghjklzxcvbnm'
    possibleUpper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    possibleDigits = '1234567890'
    possibleSpecial = '!@#$%^&*?'
    
    required = [
        random.choice(possibleLower),
        random.choice(possibleUpper),
        random.choice(possibleDigits),
        random.choice(possibleSpecial)
    ]
    
    allChars = possibleLower + possibleUpper + possibleDigits + possibleSpecial
    remaining = [random.choice(allChars) for _ in range(length - 4)]
    
    password = required + remaining
    random.shuffle(password)
    
    return ''.join(password)

def addPassword():
    
    data = loadData()
    
    site = input("Website/App name: ").strip()
    username = input("Username/Email: ").strip()
    choice = input("Auto generate a strong password? (y/n): ").strip().lower()
    
    if choice == "y":
        size = int(input("Enter password length: "))
        while size < 4:
            print("Length must be at least 4.")
            size = int(input("Enter password length: "))
        pwd = generatePassword(size)
        print(f"Generated Password: {pwd}")
    else:
        pwd = getpass("Enter password(Currently Hidden): ")
    
    data[site] = {"username": username, "password": pwd}
    saveData(data)
    print("Saved successfully")

def getPassword():
    
    data = loadData()
    site = input("Website/App name: ").strip()
    
    if site in data:
        print(f"\nSite: {site}")
        print(f"Username: {data[site]['username']}")
        print(f"Password: {data[site]['password']}")
    else:
        print("Not found")

def deletePassword():
    
    data = loadData()
    site = input("Website/App name to delete: ").strip()
    
    if site in data:
        del data[site]
        saveData(data)
        print(f"{site} deleted successfully")
    else:
        print("Not found")

def main():
    
    while True:
        print("\n1. Add Password")
        print("2. Get Password")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Choose: ")
        
        if choice == "1":
            addPassword()
        elif choice == "2":
            getPassword()
        elif choice == "3":
            deletePassword()
        elif choice == "4":
            break

main()