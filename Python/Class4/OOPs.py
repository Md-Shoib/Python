
# # 3. 
# class Person:
#     def __init__(self,name,age):
#         print("in the constructor")
#         self.name = name
#         self.age = age 
        
#     def info(self):
#         print(f"name is {self.name} and age is {self.age}")   
        
# class Student(Person):
#     def __init__(self, name, age, id):
#         super().__init__(name, age)  
#         self.id = id
               
        
# # p1 = Person("Kartik", 100)  
# # p1.info()  


 
# class Account:  # This is only the class to run we have to call the function save as we have done p1
#     def __init__(self):
#         self.__balance = 0
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
            
#     def get_balance(self):
#         return self.__balance 
    
    
# class student:  # This is only the class to run we have to call the function
#     def sound():
#         print("car is making sound")
        
# class Boat:
#      def sound():
#         print("Boat is making sound")
        
# class shoib:
#      def sound():
#         print("Plane is making sound")    
        
# # Colors and decorations 
# def outerFunc():
#     def innerFunc():
#         print("Inside inner function")
#     return innerFunc 
# func = outerFunc()

# func()


# def multiplier(a):
#     def multiply(b):
#         return a*b
#     return multiply
# double = multiplier(2)

# print(double(3))


def great_decorator(func):
    def wrapper():
        print("hello")
        func()
        print("good bye!")
    return wrapper

@great_decorator
def name():
    print("I am shoib!")
    
name()        