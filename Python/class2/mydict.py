myDict = {"name":"Student","age":100,"isStudent":True,"roll":102,"anotherDict":{
    "name":"student in innerDict",
    "age":"10",
    "isStudent":False,
    "roll":300
}}
myDict["age"]=90
print(myDict["age"])
for key,value in myDict.items():
    if key == "anotherDict":
        for inkey,inValue in value.items():
            print(f"{inkey} : {inValue}")
            break
    print(f"{key}:{value}")