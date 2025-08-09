# # function defination
# def add(num1, num2):
#     return int(num1) + int(num2)

# print(add(1,2))

# 2.How function is calling and how key word arguement work
def add(num1, num2, name):
    return f"{name} of {num1} + {num2} = {int(num1) + int(num2)}"
print(add(name="addition",num2=2,num1=1))