# #1.Sum of Number in a List 
# list= [10, 20, 30]

# Sum = sum(list)

# print("Sum of all number in a given list:", Sum)



# #2.Count vovels in a string

# text = input("Enter the string:")

# vowels = "aeiou"

# count = 0
# for char in text:
#   if char in vowels:
#     count = count + 1
    
# print("Total vowels in a string : ", count)



# #3. print multiplication table 
# num = int(input("Enter the number:"))
# print(f"Mutliplication table of {num}")

# for i in range(1,11):
#     print(f"{num}X{i} = {num * i}")



# #4. Find the maximum number from the list
# list=[2,5,1,7]
# maximum = max(list)
# print("Maximum number in the list is:", maximum)



# #5.Factorial calculator
# num = int(input("Enter the Number:"))
# fact = 1
# for i in range(1, num+1):
#     fact = fact *i  
# print(f"Factorial number of {num} is {fact}")


#Reverse the list 
mylist = [2,5,8,1]
reverselist = mylist[::-1]
print("Reverse list is:", reverselist)



# #9.palindrome number
# text = input("Enter a string:")
# # cl_text = text.lower().replace(" ", "")
# # print(cl_text)
# if text == text[::-1]:
#     print(f"{text} is palindrome")
# else:
#     print(f"{text} is not a palindrome")
    
    
    
    
# #10.Find dublicate in list
# mylist = [1,2,5,8,2,4]

# seen = set()
# dublicates = set()

# for item in mylist:
#     if item in seen:
#         dublicates.add(item)
#     else:
#         seen.add(item)
        
# print(f"Dublicate Number in list are:", list(dublicates))   


# Fizzbuzz
for i in range(1,16):
    if i % 3==0 and i % 5==0:
        print("Fizzbuzz") 
    elif i % 3==0:
        print("Fizz")
    elif i % 5==0:
        print("Buzz")
    else:
        print(i)
            
         