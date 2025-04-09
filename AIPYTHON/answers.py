
### **Q1: Create two variables, one for your name and one for your age. Print them.**

name = "Zoe"
age = 14
print(name)
print(age)

'''**Explanation**:  
`name` and `age` are variables that store text and numbers. We use `print()` to display them.
'''

### **Q2: Make a variable that holds a decimal number (like height). Print it.**
height = 5.4
print(height)
'''
**Explanation**:  
`5.4` is a **float** (decimal). Python stores it and prints it easily.
'''

### **Q3: Use math operators to add two numbers and check if one is greater than the other.**

a = 10
b = 4
print(a + b)       # 14
print(a > b)       # True
'''
**Explanation**:  
We use `+` to add, and `>` to compare values. `a > b` is **True**.
'''

## ✅ **2. Lists, Tuples, Sets, Dictionaries**
### **Q1: Make a list of your 3 favorite games. Add a new one using `.append()`.**

games = ["Minecraft", "Roblox", "Chess"]
games.append("Fortnite")
print(games)
'''
**Explanation**:  
`append()` adds an item to the end of the list.
'''

### **Q2: Create a tuple of your 3 favorite colors. Try changing one (what happens?).**

colors = ("red", "blue", "green")
# colors[0] = "yellow"  # This will give an error!
'''
**Explanation**:  
Tuples **can’t be changed** (immutable). Trying to assign a new value causes an error.
'''

### **Q3: Make a set with repeated numbers. Print it. Add a new number.**
nums = {1, 2, 2, 3}
print(nums)       # {1, 2, 3}
nums.add(4)
print(nums)       # {1, 2, 3, 4}
'''
**Explanation**:  
Sets remove duplicates automatically. `.add()` adds a unique value.
'''

### **Q4: Create a dictionary with your name, age, and favorite subject. Print the subject.**

student = {"name": "Amani", "age": 13, "subject": "Math"}
print(student["subject"])
'''
**Explanation**:  
You access a value in a dictionary using the key inside square brackets.
'''

## ✅ **3. Conditions and Loops**

### **Q1: Write an if-else to check if a number is greater than 10.**

number = 15
if number > 10:
    print("Greater than 10")
else:
    print("10 or less")
'''
**Explanation**:  
If the condition is true, the first block runs. Otherwise, the `else` block runs.
'''

### **Q2: Write a loop that prints numbers from 1 to 5.**
for i in range(1, 6):
    print(i)
'''
**Explanation**:  
`range(1, 6)` gives numbers from 1 to 5. `for` repeats the code for each number.
'''

### **Q3: Make a while loop that counts down from 3 to 1 and prints “Blast off!”**

count = 3
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
'''
**Explanation**:  
`while` repeats as long as the condition is true. `count -= 1` reduces the number.
'''

### **Q4: Area of rectangles using loop**

rectangles = [(8, 4), (5, 3), (10, 2)]
for length, width in rectangles:
    area = length * width
    print("Area of", length, "x", width, "is", area)
'''
**Explanation**:  
Each `(length, width)` pair is unpacked, area is calculated, and printed in the loop.
'''

## ✅ **4. Functions**
### **Q1: Make a function that prints “Hello! I’m learning Python!”**

def greet():
    print("Hello! I'm learning Python!")

greet()
greet()
'''
**Explanation**:  
Simple function with no parameters. Called using `greet()`.
'''

### **Q2: Function to say “Happy Birthday” to someone**

def birthday_message(name):
    print("Happy Birthday, " + name + "!")

birthday_message("Sam")
'''
**Explanation**:  
The name is passed into the function and used in the message.
'''

### **Q3: Function to double a number**

def double_number(n):
    print(n * 2)

double_number(4)

def double_number(n):
    return n * 2

result = double_number(4)
print(result)
'''
**Explanation**:  
Returning gives back the value to use later. `print()` shows it.
'''

### **Q4: Greet friend with name and age**
def greet_friend(name, age):
    message = "Hi, " + name + "! You’re " + str(age) + " years old!"
    print(message)
greet_friend("Zara", 14)
'''
**Explanation**:  
Function takes two arguments, combines into a string, and prints it.
'''

## ✅ **5. NumPy Basics**

### **Q1: Create an array with [10, 20, 30] and print it.**
import numpy as np
arr = np.array([10, 20, 30])
print(arr)

print(arr * 2)  # [20 40 60]
'''
**Explanation**:  
Multiplying a NumPy array affects all elements.
'''

### **Q2: Add all numbers in [4, 7, 6, 3] using `np.sum()`**
arr = np.array([4, 7, 6, 3])
print(np.sum(arr))  # 20
arr = np.append(arr, 10)
print(np.sum(arr))  # 30
'''
**Explanation**:  
`np.sum()` adds all elements. `np.append()` adds new values to the array.
'''

### **Q3: Multiply all values in [2, 4, 6] by 5**
arr = np.array([2, 4, 6])
result = arr * 5
print(result)  # [10 20 30]
print(np.max(result))  # 30
'''
**Explanation**:  
Multiplying scales every number. `np.max()` gives the largest value.
'''

## ✅ **6. Pandas Basics**
### **Q1: Create a table of books with Title, Author, Pages**
import pandas as pd
data = {
    "Title": ["AI for Kids", "Python Fun", "Code World"],
    "Author": ["Asha", "Ben", "Clara"],
    "Pages": [120, 150, 100]
}
books = pd.DataFrame(data)
print(books)
'''
**Explanation**:  
Pandas turns dictionaries into a table (DataFrame) for easy viewing.
'''

### **Q2: Table of students and marks – find average**
data = {
    "Name": ["Ali", "Nina", "Tom"],
    "Marks": [80, 90, 85]
}
table = pd.DataFrame(data)
print("Average Marks:", table["Marks"].mean())  # 85.0
print("Max Marks:", table["Marks"].max())  # 90
'''
**Explanation**:  
`.mean()` gets the average, `.max()` gets the highest value.
'''

### **Q3: Print only the "Name" column from the friends table**
friends = {
    "Name": ["Mia", "Leo", "Ava"],
    "Age": [13, 15, 14],
    "Score": [85, 90, 88]
}
table = pd.DataFrame(friends)
print(table["Name"])
print(table[["Name", "Age"]])
'''
**Explanation**:  
You can use one column with `table["Name"]` or multiple with `table[["Name", "Age"]]`.
'''
