📘 Week 2 – Data Structures and Functions
📌 Topics Covered

Python Data Structures

Lists: Ordered, mutable collections. Example: [1, 2, 3].

Tuples: Ordered, immutable collections. Example: (1, 2, 3).

Dictionaries: Key-value pairs. Example: {"name": "Suraj", "age": 21}.

Sets: Unordered collections of unique elements. Example: {1, 2, 3}.

Functions

Created using def.

Parameters & return values.

Lambda functions → lambda x: x*x.

Recursion → functions calling themselves.

List Comprehension

Compact way to build lists.

Example: [x*x for x in range(5)] → [0, 1, 4, 9, 16].

🖥 Hands-On Practice
✅ Program 1: Sum of Squares

This program calculates the sum of squares of numbers in a list.

# Function to calculate sum of squares
def sum_of_squares(numbers):
    return sum([x**2 for x in numbers])

nums = [1, 2, 3, 4, 5]
print("Numbers:", nums)
print("Sum of Squares:", sum_of_squares(nums))


🔹 Things Learned:

How to use list comprehensions inside functions.

Summation using Python’s built-in sum() function.

✅ Program 2: Data Cleaning (Remove Duplicates & Filter)

This script cleans a list by removing duplicates and filtering values greater than a threshold.

# Function to remove duplicates
def remove_duplicates(data):
    return list(set(data))

# Function to filter numbers greater than 10
def filter_data(data):
    return [x for x in data if x > 10]

raw_data = [5, 12, 7, 12, 18, 5, 25]
print("Raw Data:", raw_data)

cleaned_data = remove_duplicates(raw_data)
print("After Removing Duplicates:", cleaned_data)

filtered_data = filter_data(cleaned_data)
print("After Filtering (>10):", filtered_data)


🔹 Things Learned:

Using sets to remove duplicates.

Applying list comprehension for filtering.

Importance of modular functions for real-world data cleaning.

🌟 Key Takeaways

Understood the role of lists, tuples, dicts, sets in handling structured data.

Learned how functions make code reusable.

Practiced lambda, recursion, list comprehension for efficient coding.

Applied theory in a data cleaning project.

✨ Week 2 helped me move from basic Python syntax ➝ writing practical functions for data transformation & cleaning, which is a core skill in Data Science.
