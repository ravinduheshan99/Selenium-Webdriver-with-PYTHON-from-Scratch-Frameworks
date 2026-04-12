"""
python_basics.py

Purpose:
This file covers the basic Python concepts that are useful before moving into
Selenium WebDriver automation.

Topics covered:
1. Printing output
2. Variables
3. Multiple variable assignment
4. String formatting
5. data types
6. Lists
7. Tuples
8. Dictionaries

Note:
This file is written as a learning reference, so comments explain both
what the code does and why it matters.
"""

# -------------------------------------------------------------------
# 1. PRINTING OUTPUT
# -------------------------------------------------------------------
# The print() function is used to display output in the console.
print("Hello")


# -------------------------------------------------------------------
# 2. VARIABLES
# -------------------------------------------------------------------
# A variable stores a value that can be used later in the program.
number = 3
print("Value of number:", number)

message = "Hello World"
print("Value of message:", message)


# -------------------------------------------------------------------
# 3. MULTIPLE VARIABLE ASSIGNMENT
# -------------------------------------------------------------------
# Python allows assigning multiple variables in a single line.
integer_value, float_value, text_value = 5, 6.4, "Great"

# Printing variable values using the format() method.
# This is a clean way to combine strings and other data types.
print("{} {}".format("Value of integer_value is:", integer_value))
print("{} {}".format("Value of float_value is:", float_value))
print("{} {}".format("Value of text_value is:", text_value))


# -------------------------------------------------------------------
# 4. CHECKING DATA TYPES
# -------------------------------------------------------------------
# type() is used to find the data type of a variable.
print("Type of integer_value:", type(integer_value))   # int
print("Type of float_value:", type(float_value))       # float
print("Type of text_value:", type(text_value))         # str


# -------------------------------------------------------------------
# 5. COMMON PYTHON DATA TYPES
# -------------------------------------------------------------------
# Some common Python data types:
# int      -> whole numbers
# float    -> decimal numbers
# complex  -> complex numbers
# str      -> text
#
# In Selenium projects, you will often work with strings, lists,
# dictionaries, booleans, and sometimes numeric values.


# -------------------------------------------------------------------
# 6. LISTS
# -------------------------------------------------------------------
# A list can store multiple values in a single variable.
# A list:
# - keeps order
# - allows duplicate values
# - can contain mixed data types
# - is mutable, meaning values can be changed
values = [1, 2, "Ravindu", 3, 4.5]

# Accessing list elements using index positions
print("First item:", values[0])
print("Third item:", values[2])
print("Last item:", values[-1])  # Refers to the last index

# Slicing a list
# This returns items from index 2 up to, but not including, index 4
print("Sliced values (index 2 to 3):", values[2:4])

# Inserting a value at a specific index
values.insert(3, "Haputhanthri")
print("After insert:", values)

# Appending adds a value to the end of the list
values.append("End")
print("After append:", values)

# Updating a value in the list
values[2] = "RAVINDU"
print("After update:", values)

# Deleting a value from the list using its index
del values[0]
print("After delete:", values)


# -------------------------------------------------------------------
# 7. TUPLES
# -------------------------------------------------------------------
# A tuple is similar to a list, but it is immutable.
# Immutable means its values cannot be changed after creation.
tuple_values = (1, 2, "Ravindu", 4.5)

print("Value at index 2 in tuple:", tuple_values[2])

# The following line would cause an error because tuples do not support item assignment:
# tuple_values[2] = "RAVINDU"


# -------------------------------------------------------------------
# 8. DICTIONARIES
# -------------------------------------------------------------------
# A dictionary stores data in key-value pairs.
# Each key is used to access its related value.
person_dictionary = {"a": 2, 2: "Ravindu", "c": "Haputhanthri"}

print("Value for key 'a':", person_dictionary["a"])
print("Value for key 2:", person_dictionary[2])
print("Value for key 'c':", person_dictionary["c"])

# Creating an empty dictionary and adding values step by step
name_dictionary = {}
name_dictionary["firstName"] = "Ravindu"
name_dictionary["secondName"] = "Haputhanthri"

print("Name dictionary:", name_dictionary)