# WAP to find the greatest of four number enterd by user.
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))
d = int(input("Enter the number:"))

if(a>b and a>c and a>d):
    # print(f"A is the greatest number : {a}")
    print("A is the greates number ", a)
    
elif(b>a and b>c and b>d):
    print(f"B is the greatest number:{b}")  # I used here f as f-string is helps to print the values as well 
    
elif(c>a and c>b and c>d):
    print("C is the greatest number")

else :
    print("D is the greatest number")