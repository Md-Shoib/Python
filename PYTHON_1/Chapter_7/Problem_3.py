# # Factorial number 
# num = int(input("Enter the number:"))
# i=1
# fact = 1
# while(i<=num):
#     fact = fact * i
#     i+=1
# print(fact)



# Factorail number using for loop 
num = int(input("Enter the number:"))
fact = 1
for i in range (1, num+1):
    fact = fact * i
    i = i+1
    
print("Factorail Number is : ",fact)    