import random

def generatePassword (length):
    
    possibleChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*?'
    
    password = ''
    
    for i in range (length):
        password += random.choice(possibleChars)
    
    return password

size = int(input("Enter random password length:"))

password = generatePassword (size)

print (f"Your random password is: {password}")