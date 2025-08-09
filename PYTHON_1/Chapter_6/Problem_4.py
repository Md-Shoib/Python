# # WAP to take user name and check where it contain 10 character or not
# user_name = input("Enter the User name:")
# len(user_name)
# if(len(user_name)>10):
#     print("IT Contain more character")
# else:
#     print("Not")
    


# Make a list and check whether his/her name is in the list or not
import emoji
li = input("Enter the name in the list seperated by comma :").split(',')

name = input("Enter Your name : ")
if(name in li):
    print(emoji.emojize("Be Happy :smile: your name is in the list", language='alias'))
else:
    print(emoji.emojize("Your name is not in the list :cold_sweat:", language='alias'))
    