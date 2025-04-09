

### Introduction to Python Libraries for AI
'''
- Libraries are like superpowers for Python.
- Pandas: Great for organizing data in tables.
'''
#### How to Use NumPy and Pandas
'''
- Install it (just once):
  - In a terminal, type: `pip install pandas`.
- Then use it in your code!
'''

#### Pandas Example: Working with Data
import pandas as pd  # Load the data toolkit
# Make a table of friends
data = {
    "Name": ["Mia", "Leo", "Ava"],
    "Age": [13, 15, 14],
    "Score": [85, 90, 88]
}
table = pd.DataFrame(data)
print("Friends Table:")
print(table)
print("Average Score:", table["Score"].mean())  # Find the average score

#Explanation:
'''
- `pd.DataFrame(data)` turns the dictionary into a table.
- `table["Score"].mean()` calculates the average of the "Score" column.
'''


'''
1. Create a table of 3 books using Pandas.
Each book should have a Title, Author, and Pages.
2. Given a table of students and their marks, use Pandas to calculate the average mark.
3. Use the friends table example.
Print only the "Name" column using Pandas.
'''