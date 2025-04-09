
#### 5. Lists
'''
- A list is like a shopping list—a collection of items you can change.
- Use square brackets `[]` and commas to separate items.

'''

#Example:
# A list of favorite foods
foods = ["pizza", "ice cream", "tacos"]
print(foods)         # Show the whole list
print(foods[0])      # Show the first item (pizza)
foods.append("cake") # Add a new item
print(foods)         # See the updated list

#Explanation:
'''
- `foods[0]` gets the first item (counting starts at 0!).
- `.append()` adds something new to the end.
'''


#### 6. Tuples
'''
- A tuple is like a list, but you *can’t change it* after making it.
- Use parentheses `()` instead of brackets.
'''
#Example:
# A tuple of coordinates
point = (3, 4)
print(point)     # Show the tuple
print(point[1])  # Show the second item (4)
# point[1] = 5   # This would cause an error because tuples can’t change!


#Explanation:
'''
- Tuples are locked—great for things that shouldn’t change, like a point on a map.
'''


#### 7. Sets
'''
- A set is a collection with *no duplicates*, like a unique club.
- Use curly braces `{}` or `set()`.
'''
#Example:
# A set of numbers
numbers = {1, 2, 2, 3}  # Notice 2 is repeated
print(numbers)          # Shows {1, 2, 3}—no duplicates!
numbers.add(4)          # Add a new number
print(numbers)          # Shows {1, 2, 3, 4}


#Explanation:
'''
- Sets automatically remove repeats.
- `.add()` puts a new item in.
'''



#### 8. Dictionaries
'''
- A dictionary is like a mini phonebook—each item has a *key* (like a name) and a *value* (like a phone number).
- Use curly braces `{}` with `key: value` pairs.
'''
#Example:
# A dictionary of student info
student = {"name": "Mia", "age": 13, "grade": 8}
print(student)         # Show the whole dictionary
print(student["name"]) # Show just the name (Mia)
student["age"] = 14    # Update the age
print(student)         # See the updated dictionary


#Explanation:
'''

- `student["name"]` looks up the value for the "name" key.
- You can change values by assigning a new one.

'''
'''
Questions
1. Create a list of 3 favorite animals.
Then:
Print the full list.
Print the second animal.
Add one more animal using .append() and print the new list.

2. Create a tuple called location with two numbers (like coordinates: 7, 9).
Then:
Print the whole tuple.
Print just the second number.
Try to change one number. What error do you get?

3. Create a dictionary for yourself with keys "name", "age", and "hobby".
Then:
Print your name from the dictionary.
Change your hobby to something new.
Print the full updated dictionary.
'''