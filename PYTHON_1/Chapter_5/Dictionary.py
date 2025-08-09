# Dictionary in Python is mutable, Unorder and index collection of key value pair 


# # Example 1)
# marks = {
#     "Shoib": 80,
#     "Sakir": 75,
#     "Kartik": 70
# }
# print(marks, type(marks))
# print(marks)



#In Dictionary we an update on dist directly using update an it change the exiting list 
marks = {
    "Shoib": 80,
    "Sakir": 75,
    "Kartik": 70
}
print(marks, type(marks))
marks.update({"Shoib": 85})  #Used to update(Method) the list 
print(marks)
print(marks.values())  # Show all the values of dict
print(marks.items())   # Retuna key and value of the dict
print(marks.pop('Kartik')) # It helps to return the value of particular key 
print(marks.popitem())




#Some useful Dictionary method from ChatGpt
# | Method                   | Description                                 |
# | ------------------------ | ------------------------------------------- |
# | `dict.get(key, default)` | Returns value for key; default if not found |
# | `dict.keys()`            | Returns all keys                            |
# | `dict.values()`          | Returns all values                          |
# | `dict.items()`           | Returns list of `(key, value)` tuples       |
# | `dict.update()`          | Merges another dictionary                   |
# | `dict.pop(key)`          | Removes item with given key                 |
# | `dict.clear()`           | Empties dictionary                          |



