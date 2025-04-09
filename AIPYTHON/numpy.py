

### Introduction to Python Libraries for AI
'''
- Libraries are like superpowers for Python.
- NumPy is a Python library.
- NumPy is used for working with arrays.
- NumPy is short for "Numerical Python".
- NumPy: Awesome for math and numbers.
'''
#### How to Use NumPy
'''
- Install it (just once):
  - In a terminal, type: `pip install numpy`.
- Then use it in your code!
'''
#### NumPy Example: Playing with Numbers
import numpy as np  # Load the math toolkit

numbers = np.array([1, 2, 3, 4, 5])  # Make a list of numbers
print("Numbers:", numbers)
print("Triple:", numbers * 3)         # Triple every number
print("Sum:", np.sum(numbers))        # Add them all up


#Explanation:
'''
- `np.array()` creates a special list.
- `numbers * 3` multiplies every number at once.
- `np.sum()` adds everything together.
'''

'''
1. Use np.array() to create an array with these numbers: 10, 20, 30.
Print the array.
2. Make a NumPy array with [4, 7, 6, 3].
Then use np.sum() to print the total.
3. Create an array of numbers: [2, 4, 6]
Multiply every number in the array by 5, and print the new result.

'''