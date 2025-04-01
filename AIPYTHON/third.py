###Conditions
### If ... Else
'''
Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
'''
#Example
a = 33
b = 200
if b > a:
  print("b is greater than a")

#### Elif
'''
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
'''
#Example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

### Else
'''
The else keyword catches anything which isn't caught by the preceding conditions.
'''
#Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

'''
In this example a is greater than b, so the first condition is not true, also the elif condition is not true,
 so we go to the else condition and print to screen that "a is greater than b".
'''




#### 9. Loops
'''
- Loops let you repeat things without writing the same code over and over.
- Two main types:
  - **for loop**: Repeats for each item in a list, set, etc.
  - **while loop**: Repeats as long as something is true.
'''
#For Loop Example:
# Print each food in the list
foods = ["pizza", "ice cream", "tacos"]
for food in foods:
    print("I like", food)


#While Loop Example:
# Count down from 3
count = 3
while count > 0:
    print(count)
    count = count - 1  # Decrease by 1 each time
print("Blast off!")


#Explanation:
'''
- `for food in foods`: Takes each item one-by-one.
- `while count > 0`: Keeps going until `count` hits 0.
'''

#### 12. Coding Exercise 2: Calculating Area with a Loop
'''
Let’s calculate areas for multiple rectangles.
'''
# Calculate areas for different rectangles
rectangles = [(8, 4), (5, 3), (10, 2)]  # List of tuples (length, width)
for length, width in rectangles:
    area = length * width
    print("Area of", length, "x", width, "is", area)
