# #1) Write a python program to display user name followed by doog Afternoon write the code in the proper way that can be managed properly 
# first_name = input("Enter your first name:")
# last_name = input("Enter your last name:")
# final = first_name + " " + last_name
# reversed = last_name + first_name
# print("Name of the user is:",final, reversed)

# #2) Detect the double space in a string 
# name = input("Enter the sentence:")
# print(name.find("is"))


# #3) how to make the list 
# user_list = input("Enter the list of fruits: ")
# my_list = user_list.split()
# print(my_list[1:4])


# #4) How to add the item in the list 
# my_list = input("Enter the item").split() 
# # .split() is used to make a list of items 
# my_list.append("Harry")
# print("List after adding:", my_list)




# #5) How to sort the item of list and reverse the list
# my_list = input("Enter the number:").split()
# my_list.sort() 
# # .sort method is used to sort the item
# print(my_list)
# my_list.reverse()
# # .reverse method is used to reverse the list the list 
# print(my_list)

# my_list.pop()
# # .pop method is used to delete the items from th list 
# print(my_list)
 


# #6) .split is only used in string not in integer to use it in integer we have to convert it
# my_list= input("Enter the items for list").split()
# # str_list = my_list.split()           # Split in to list of string 
# int_list=[int(x) for x in my_list]  # Convert the string in list 
# int_list.sort()
# print("Sorted list:",int_list)
# int_list.reverse()
# print("Reverse list:", int_list)
# print("Total length of list:",len(int_list))


# #7) Tuple : is a Imutable means we can take a list of item but can not change the original list copy the another list 
# user_input = input("Enter the number:")
# my_input = tuple(int(i) for i in user_input.split()) # This used to convert the string input into integer 
# print("MY Tuple list: ", my_input)
# # In case of strings
# my_input = tuple(user_input.split())
# print("My Tuple for strings :", my_input)


# # Some tuple question
# t = (1, 2, 3, 2, 4)
# print(t.count(2))      # 2
# print(t.index(3))      # 2
# print(len(t))          # 5
# print(t[1:4])          # (2, 3, 2)
# print(t + (5, 6))      # (1, 2, 3, 2, 4, 5, 6)
# print(4 in t)          # True

