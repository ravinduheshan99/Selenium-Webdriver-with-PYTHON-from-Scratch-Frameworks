"""
File: 03_python_functions.py

Purpose:
This file covers the basics of functions in Python, which are essential for
writing reusable and maintainable code in Selenium automation.

Topics covered:
1. What is a function
2. Function declaration
3. Function parameters
4. Function return values
5. Function calling

Note:
Functions are widely used in Selenium frameworks to avoid code duplication
and to organize test logic into reusable components.
"""

# -------------------------------------------------------------------
# 1. WHAT IS A FUNCTION
# -------------------------------------------------------------------
# A function is a block of reusable code that performs a specific task.
# Instead of writing the same code multiple times, we define a function
# once and call it whenever needed.


# -------------------------------------------------------------------
# 2. FUNCTION DECLARATION WITH PARAMETER
# -------------------------------------------------------------------
# This function takes a name as input and prints a greeting message.
def greet_user(name):
    print("Good Morning " + name)


# -------------------------------------------------------------------
# 3. FUNCTION WITH RETURN VALUE
# -------------------------------------------------------------------
# This function takes two numbers as input and returns their sum.
def add_integers(first_number, second_number):
    return first_number + second_number


# -------------------------------------------------------------------
# 4. FUNCTION CALLING
# -------------------------------------------------------------------
# Calling the function with a specific value.
greet_user("Ravindu Haputhanthri")

# Calling the function and printing the returned result.
result = add_integers(10, 20)
print("Sum of given numbers:", result)