"""
python_oops_classes.py

Purpose:
Understanding classes, constructor, and variables in Python from a Java perspective.
"""

class Calculator:

    num = 100  # Class variable (similar to static variables in Java)

    def __init__(self, a, b):
        # In Python, __init__ acts like a constructor (no explicit constructor name like Java)
        # 'self' is equivalent to 'this' in Java and is required to access instance variables
        self.first_number = a
        self.second_number = b

        print("Constructor executed when object is created")

    def get_data(self):
        print("Method execution from Calculator class")

    def calculate_sum(self):
        # Accessing class variable using ClassName (similar to static access in Java)
        return self.first_number + self.second_number + Calculator.num


# Object creation
# No 'new' keyword is required in Python (unlike Java)
calculator = Calculator(2, 3)

# Accessing class variable
print("Class variable:", calculator.num)

# Calling instance method
calculator.get_data()

# Calling method with return value
result = calculator.calculate_sum()
print("Result:", result)