# file operation


# 1.print in the same line of all the content
file = open("./class3/db.txt") #It is used to read the file and path is nessary 

content = file.read()
content = file.readlines()

print(content)
file.close()



# 2.Print in the next line
file = open("./class3/db.txt")

content = file.readlines()

for line in content: #This i used to print the text in next line 
    print(line)

file.close()



# 3.Print in the Index
file = open("./class3/db.txt") #It is used to read the file and path is nessary 

content = file.readlines()

for line in range(0,len(content)):
    print(content[line])
    
file.close()    