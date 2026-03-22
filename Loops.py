"""
File: 02_python_control_flow_loops.py

Purpose:
This file covers Python control flow concepts that are important before moving
into Selenium WebDriver automation.

Topics covered:
1. if-else conditions
2. Comparison operators
3. for loops
4. range() usage
5. while loops
6. break statement
7. continue statement

Note:
This file is written as a learning reference, so comments explain both
what the code does and why it matters.
"""

# -------------------------------------------------------------------
# 1. IF-ELSE CONDITION WITH STRINGS
# -------------------------------------------------------------------
# if-else is used to execute different blocks of code based on a condition.
greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition Matches")
else:
    print("Condition Does Not Match")

print("1st if-else condition code is completed")
print("****************************************")


# -------------------------------------------------------------------
# 2. IF-ELSE CONDITION WITH NUMBERS
# -------------------------------------------------------------------
# Comparison operators such as >, <, ==, != are commonly used in conditions.
number = 4

if number > 2:
    print("Condition Matches")
else:
    print("Condition Does Not Match")

print("2nd if-else condition code is completed")
print("****************************************")


# -------------------------------------------------------------------
# 3. FOR LOOP WITH A LIST
# -------------------------------------------------------------------
# A for loop is used to iterate through each item in a collection.
numbers = [1, 3, 5, 7, 9]

for value in numbers:
    print(value * 2)

print("1st for loop code is completed")
print("******************************")


# -------------------------------------------------------------------
# 4. FOR LOOP WITH range()
# -------------------------------------------------------------------
# Example: sum of first natural numbers
# 1 + 2 + 3 + 4 + 5
#
# range(start, stop) generates numbers from start to stop - 1
summation = 0

for current_number in range(1, 6):
    summation = summation + current_number

print("Sum of first five natural numbers:", summation)

print("2nd for loop code is completed")
print("******************************")


# -------------------------------------------------------------------
# 5. FOR LOOP WITH range() AND STEP VALUE
# -------------------------------------------------------------------
# range(start, stop, step) allows control over the increment.
# Here, the loop prints odd numbers from 1 to 9.
for odd_number in range(1, 10, 2):
    print(odd_number)

print("3rd for loop code is completed")
print("******************************")


# -------------------------------------------------------------------
# 6. FOR LOOP USING DEFAULT range()
# -------------------------------------------------------------------
# range(10) starts from 0 and goes up to 9.
for index in range(10):
    print(index)

print("4th for loop code is completed")
print("******************************")


# -------------------------------------------------------------------
# 7. WHILE LOOP
# -------------------------------------------------------------------
# A while loop runs as long as the given condition remains True.
counter = 4

while counter > 1:
    if counter != 3:
        print(counter)

    counter = counter - 1

print("1st while loop code is completed")
print("********************************")


# -------------------------------------------------------------------
# 8. WHILE LOOP WITH break
# -------------------------------------------------------------------
# break is used to exit the loop immediately when a condition is met.
counter_with_break = 10

while counter_with_break > 1:
    print(counter_with_break)

    if counter_with_break == 3:
        break

    print(counter_with_break)
    counter_with_break = counter_with_break - 1

print("2nd while loop code is completed")
print("********************************")


# -------------------------------------------------------------------
# 9. WHILE LOOP WITH continue AND break
# -------------------------------------------------------------------
# continue skips the current iteration and moves to the next one.
# break stops the loop completely.
counter_with_continue = 10

while counter_with_continue > 1:
    if counter_with_continue == 9:
        counter_with_continue = counter_with_continue - 1
        continue

    if counter_with_continue == 3:
        break

    print(counter_with_continue)
    counter_with_continue = counter_with_continue - 1

print("3rd while loop code is completed")
print("********************************")