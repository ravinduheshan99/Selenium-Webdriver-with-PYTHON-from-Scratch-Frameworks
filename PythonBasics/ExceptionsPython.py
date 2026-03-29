"""
python_exception_handling.py

Purpose:
Understanding exception handling in Python, which is essential for
robust test automation and error handling.

Topics covered:
1. Raising exceptions
2. Assertions
3. try-except blocks
4. Exception capturing
5. finally block
"""

# -------------------------------------------------------------------
# 1. MANUAL VALIDATION USING EXCEPTION / ASSERT
# -------------------------------------------------------------------
items_in_cart = 0

# Similar to Java: throwing an exception manually
# if items_in_cart != 2:
#     raise Exception("Product cart count not matching")

# Assertion (commonly used in test validations)
# In Python, assert is widely used in frameworks like pytest
# assert items_in_cart == 2


# -------------------------------------------------------------------
# 2. BASIC TRY-EXCEPT
# -------------------------------------------------------------------
# Equivalent to try-catch in Java
try:
    with open('file.txt', 'r') as reader:
        reader.read()
except:
    # Avoid using bare except in real projects, but useful for learning
    print("Execution failed inside try block")


# -------------------------------------------------------------------
# 3. TRY-EXCEPT WITH EXCEPTION OBJECT
# -------------------------------------------------------------------
# Recommended approach: capture the actual exception
try:
    with open('file.txt', 'r') as reader:
        reader.read()
except Exception as e:
    # Similar to catching Exception e in Java
    print("Error message:", e)


# -------------------------------------------------------------------
# 4. FINALLY BLOCK
# -------------------------------------------------------------------
# finally always executes, regardless of success or failure
# Used for cleanup actions (closing resources, logging, etc.)
finally:
    print("Cleaning up resources")