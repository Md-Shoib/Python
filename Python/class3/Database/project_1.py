# Text base database 

# Above code is to create a password 
import random # This 

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
number = "0123456789"
spchs = "!@#$%&"
password=""

# This function is used to create the password
def genuid():
    uid = ""
    for i in range(4):
        char = letters[random.randint(0,51)]
        uid += char
    for i in range(3):
        char = number[random.randint(0,9)]
        uid += char
    for i in range(3):
        char = spchs[random.randint(0,5)]
        uid += char
    uidList = list(uid)
    random.shuffle(uidList)
    suffpass = "".join(uidList)
 
    return suffpass

           
# This function is used to create the data base
def create_database(filename):
    with open(filename) as file:
        file.write("id,name,email\n")
    print("database created.")
    
def add_user(filename,name, email):
    with open(filename,"a") as file:
        file.write(f"{genuid()},{name},{email}\n")
    print("user added.")
    
def read_database(filename):
    with open(filename,"r") as file:  
        content = file.readlines()
        for line in content:
            print(line) 
            
# This function is used to search  
def search_user(filename, user_id):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            user = line.strip().split(",")
            if user[0] == str(user_id):
                print(f"user FoundL ID:{user[0]}, Name:{user[1]}, Email:{user[2]}")  
                
# This function is used to update the user name or password  
def update_user(filename, user_id, new_name, new_email):
    updated = False
    with open(filename, "r") as file:
        lines = file.readlines()
        
    with open(filename, "w") as file:
        for line in lines:
            user = line.strip().split(",")
            if user[0] == str(user_id):
                file.write(f"{user_id},{new_name}, {new_email}\n")
                updated = True
            else:
                file.write(line)
    print("User updated." if updated else "User not founded!") 
    
    
# This function is used to delete the information 
def delete_user(filename,user_id):
    deleted = False
    with open(filename, "r") as file:
        lines = file.readlines()
        
    with open(filename, "w") as file:
        for line in lines:
            user = line.strip().split(",")
            if user[0] != str(user_id):
                file.write(line)
            else:
                deleted = True
    print("User deleted." if deleted else "User not founded!") 
            
                                                  
            
filename = "db.txt"              
            
add_user(filename, "kartik", "kartik71@gmail.com")
add_user(filename, "Shoib", "shoib123@gmail.com")
read_database(filename)      