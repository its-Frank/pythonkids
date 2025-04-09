
#### 10. Functions
'''
- A function is like a recipe—you write it once and use it whenever you want.
- Use `def` to define it, then call it by name.
- You can pass data, known as parameters, into a function.
- To call a function, use the function name followed by parenthesis:
- A parameter is the variable listed inside the parentheses in the function definition.
- An argument is the value that is sent to the function when it is called.
'''
#Example:
# A function to say hello
def say_hello(name):
    message = "Hello, " + name + "!"
    print(message)

# Use the function
say_hello("Leo")  # Prints "Hello, Leo!"
say_hello("Ava")  # Prints "Hello, Ava!"


#Explanation:
'''
- `def say_hello(name)`: Creates a function that takes a "name" as input.
- Call it with `say_hello("Leo")` to run the recipe with "Leo".
'''
#### 11. Coding Exercise 1: Printing Messages
'''
Let’s use variables and a function to greet someone!
'''
# Greet a friend with a function
def greet_friend(name, age):
    message = "Hi, " + name + "! You’re " + str(age) + " years old!"
    print(message)

greet_friend("Zara", 14)

'''
Questions:
1. Create a function called greet_me() that takes no parameters.
Inside, print a message like: "Hello! I'm learning Python!"
Then, call the function.

2. Create a function called birthday_message(name) that prints:
"Happy Birthday, <name>!"

3. Create a function called double_number(n) that prints double the number given.

'''