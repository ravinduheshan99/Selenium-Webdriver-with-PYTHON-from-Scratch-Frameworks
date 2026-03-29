"""
python_file_handling.py

Purpose:
Understanding file handling in Python for reading test data and writing outputs.
"""

# -------------------------------------------------------------------
# 1. BASIC FILE READING METHODS
# -------------------------------------------------------------------
file = open('read.txt')

# Read entire file
# print(file.read())

# Read first n characters
# print(file.read(2))

# Read line by line
# print(file.readline())
# print(file.readline())

# Using while loop to read file
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# Recommended: readlines() (returns list)
for line in file.readlines():
    print(line)

file.close()


# -------------------------------------------------------------------
# 2. FILE HANDLING USING 'with' (RECOMMENDED APPROACH)
# -------------------------------------------------------------------
# 'with open' automatically handles file closing (similar to Java try-with-resources)
with open('read.txt', 'r') as reader:
    content = reader.readlines()

    # Normalize lines to avoid newline issues (important in real-world data handling)
    cleaned_content = [line.strip() for line in content]

    # Explicitly clear file before writing (even though 'w' does this implicitly)
    with open('write.txt', 'w') as writer:
        writer.truncate(0)

    # Reverse and write content safely
    with open('write.txt', 'w') as writer:
        for line in reversed(cleaned_content):
            writer.write(line + '\n')


# -------------------------------------------------------------------
# 3. VERIFY OUTPUT FILE
# -------------------------------------------------------------------
with open('write.txt', 'r') as reader:
    for line in reader.readlines():
        print(line)