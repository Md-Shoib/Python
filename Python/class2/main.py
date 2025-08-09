# crud operation

import time
db = []
# create
def createEntry(bookName,issueDate,renewDate,assignPerson):
    entry = {
        "bookName": bookName,
        "issueDate":issueDate,
        "renewDate":renewDate,
        "assignPeron":assignPerson,
        "id":id
    }
    db.append(entry)
 
# delete
def deleteEntry(id):
    for i, item in enumerate(db):
        if item["id"]==id:
            del db[i]
            break
        
#read
def displayentries():
    for i, item in enumerate(db):
        print("id:",item["id"]) 
        print("bookName:",item["bookName"])
        print("assignPerson:",item["assignPerson"])
        print("issueDate:",item["issueDate"])
        print("renewDate:",item["renewDate"])
        print(".........................................")

#search
def search(name):
    for i, item in enumerate(db): 
        if item["assignPerson"]==name:   
            print("id:",item["id"]) 
            print("bookName:",item["bookName"])
            print("assignPerson:",item["assignPerson"])
            print("issueDate:",item["issueDate"])
            print("renewDate:",item["renewDate"])
            print(".........................................")
            
#update
def updateEntry(id,assignPerson="",issueDate="",renewDate=""):
    for i, item in enumerate(db):
        if item["id"] == id:
            if item["assignPerson"] !="" :
                item["assignPerson"] = assignPerson
            if item["issueDate"] !="" :
                item["issueDate"] = issueDate
            if item["renewDate"] !="":
                    item["renewDate"] =renewDate
                

# Interface
while True:
    ops = input("press [y] for entry or press [e] for exit:")
    
    print("press [c] to create entry: ")
    print("press [d] to display all entry: ")
    print("press [s] to search entries: ")
    print("press [x] to delete entries: ")
    print("press [u] to update entries: ")
    
    if ops == "c" or ops == "C":
        id = input("Enter book id:")
        bookName = input("Enter book name:")
        assignPerson = input("Enter assign book person name:")
        issueDate = time.ctime()
        renewDate = input("Enter assign ")
        createEntry(bookName,assignPerson,issueDate,renewDate)
        
        
    if ops == "d" or ops == "D":
       displayentries()
    
    if ops == "s" or ops == "S":
        name=input("Enter person name to search:")
        search(name)
    
    if ops == "x" or ops == "X":
        id=input("Enter book id to create :")
        deleteEntry(id)
    
    if ops == "e" or ops == "E":
        break
    