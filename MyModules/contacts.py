import re

def isValidName(name):
    pattern = '^[A-Za-z\s]*' 
    if re.search(pattern,name):
        return True
    return False

def isValidMobile(mno):
    pattern = '^[6-9]\d{9}$'
    if re.search(pattern, mno):
        return True
    return False

path = "MyFiles/contact.txt"

def createContact(name, contact):
    if isValidName(name) and isValidMobile(contact):
        with open(path, 'a') as fh:
            fh.write(name + " : " + contact + "\n")
            print("Contact Saved")
    else:
        print("Error: Invalid details")
        
def allContacts():
    with open(path,'r') as fh:
        for line in fh:
            print(line.rstrip())
            
def searchContact(name):
    with open(path,'r') as fh:
        for line in fh:
            ct = line.split()
            if ct[0] == name:
                return 'Contact: ' + ct[2]                
        return 'No Contact exists';