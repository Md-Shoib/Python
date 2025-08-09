# In Python, a set is an unordered collection of unique elements. It is mutable, meaning you can add or remove items, but the elements themselves must be immutable (like numbers, strings, or tuples).

# METHODS OF SETS 
# | Method                             | Description                                           |                                               |
# | ---------------------------------- | ----------------------------------------------------- | --------------------------------------------- |
# | `add(elem)`                        | Adds a single element to the set                      |                                               |
# | `update(iterable)`                 | Adds multiple elements from another iterable          |                                               |
# | `remove(elem)`                     | Removes an element; raises error if not found         |                                               |
# | `discard(elem)`                    | Removes an element; does NOT raise error if not found |                                               |
# | `pop()`                            | Removes and returns a random element                  |                                               |
# | `clear()`                          | Removes all elements                                  |                                               |
# | `copy()`                           | Returns a shallow copy of the set                     |                                               |
# | `union(*sets)` or \`               | \`                                                    | Returns a new set with elements from all sets |
# | `intersection(*sets)` or `&`       | Returns a set with common elements                    |                                               |
# | `difference(*sets)` or `-`         | Returns a set with elements not in other(s)           |                                               |
# | `symmetric_difference(set)` or `^` | Returns elements in either set, but not both          |                                               |
# | `issubset(set)` or `<=`            | Checks if current set is subset of another            |                                               |
# | `issuperset(set)` or `>=`          | Checks if current set is superset of another          |                                               |
# | `isdisjoint(set)`                  | Returns True if sets have no common elements          |                                               |




# # Some METHOD of Set 
# my_set_1 = {1,5,8,'shoib'}
# my_set_2 = {4,2,8,'alam'}

# my_set_1.add('alam')
# my_set_2.add('shoib')  # It is used to add the item in the list 
# print(my_set_1,my_set_2)

# my_set_1.update(['md']) # It update the existing list
# my_set_2.update([2])  # Set doest not contain the repeted value. So, It is will not print 2 one more time.
# print(my_set_1,my_set_2)

# my_set_1.pop()
# my_set_2.pop()
# print(f"It Will remove random elemnts {my_set_1,my_set_2}")

# my_set_1.clear()
# my_set_2.clear()
# print(f"It will clear the all the elemt from the set {my_set_1,my_set_2}")




# OPERATION of SET (Taking a input from the user)
user_input_1 = input("Enter the elements for set one:") # Taking a user input 
set_1 = set(int(x) for x in user_input_1.split())          #.split is used to take a multiple integer and also conveting string in to int 
user_input_2 = input("Enter the elements for set Two:")
set_2 = set(int(x) for x in user_input_2.split())

# print(set_1.union(set_2))    ...#OR 
result = set_1.union(set_2)
print("The Union of the set is:", result)  #...OR

print(f"The Intersection of the set is :{set_1.intersection(set_2)}")  #Here f is f-String which is used to embed expression (like variable, Function call , or calculation)









