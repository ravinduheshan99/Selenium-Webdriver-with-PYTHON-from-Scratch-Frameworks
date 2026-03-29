"""
python_inheritance.py

Purpose:
Understanding inheritance in Python and how it compares with Java OOP concepts.
"""

from PythonOOP import Calculator


class ChildImpl(Calculator):

    num2 = 200  # Class variable (similar to static variable in Java)

    def __init__(self):
        # In Python, constructor overriding is similar to Java,
        # but parent constructor is called explicitly
        print("Child class constructor executed")

        # This is equivalent to super() in Java, but more Pythonic way is super().__init__()
        Calculator.__init__(self, 2, 3)

    def get_complete_data(self):
        # Accessing:
        # - child class variable (num2)
        # - parent class variable (num)
        # - parent class method (Summation)
        return self.num2 + self.num + self.Summation()


# Object creation (no 'new' keyword in Python)
child = ChildImpl()

# Calling method that uses inherited + own properties
print("Final Value:", child.get_complete_data())