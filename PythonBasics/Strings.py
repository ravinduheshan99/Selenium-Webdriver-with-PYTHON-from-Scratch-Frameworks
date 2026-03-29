"""
python_strings.py

Purpose:
Understanding common string operations in Python and how they compare
to Java string handling in automation scenarios.
"""

str1 = "RavinduHaputhanthriAcademy.com"
str2 = "Consulting Firm"
str3 = "RavinduHaputhanthri"

# Indexing (similar to charAt in Java, but returns a string instead of char)
print(str1[1])

# Slicing (Python way of substring, end index is exclusive)
print(str1[0:7])

# Concatenation (same as Java using + operator)
print(str1 + str2)

# Substring check (cleaner than Java contains() method)
print(str3 in str1)


# Splitting string (similar to split() in Java)
split_values = str1.split(".")
print(split_values)
print(split_values[0])


# Trimming spaces
str4 = "great1 "
print(str4.strip())   # removes spaces from both sides (like trim() in Java)

str5 = " great2 "
print(str5.lstrip())  # removes leading spaces
print(str5.rstrip())  # removes trailing spaces