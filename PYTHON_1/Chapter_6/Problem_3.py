# Detect the Spam message or comment 
import emoji


c1 = "Make a lot of Money"
c2 = "Subscribe the channel"
c3 = "A lot of Money"
c4 = "Lucky draw"

user_input = input("Enter the Comment! :")

if((user_input in c1) or (user_input in c2) or (user_input in c3) or (user_input in c4)):
    print("This is spam comment")
    print(emoji.emojize("BE carefull :scream: :moyai:!", language='alias')) # This is amazing use can use any emoji I have already install the emoji library

else:
    print(emoji.emojize("Thank you For your comment :blush: ", language='alias'))