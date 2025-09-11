# # Task 1: Read a File and Handle Errors 
# # Problem Statement:  Write a Python program that:
# # 1.   Opens and reads a text file named sample.txt.
# # 2.   Prints its content line by line.
# # 3.   Handles errors gracefully if the file does not exist.

# # Condition 1 
# # If the file exist
with open('sample.txt','r') as file:
    reading_file = file.read()
print (reading_file)

# # Condition 1 Answer:
Line 1 = Hi
Line 2 = Welcome to the python series

# # Condition 2 
# # If the file does not exist
file1 = open('sample.txt','r')
if 'content' == file1.read():
    print (content)
else: 
    print ("The file sample.txt is not found")

# # Condition 2 Answer:
The file sample.txt is not found


# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.



def file_operations():
    file_name = "output.txt"
user_initial_input = input("Enter the initial content to write to the file: ")
with open('file_name', 'w') as file:
    file.write(user_initial_input + "\n")
    print(f"Initial content written to '{'file_name'}'.")

# 2. Appends additional data to the same file
additional_data = input("Enter additional data to append to the file: ")
with open('file_name', 'a') as file:
    file.write(additional_data + "\n")
    print(f"Additional data appended to '{'file_name'}'.")

# 3. Reads and displays the final content of the file
print(f"\nReading the final content of '{'file_name'}':")
with open('file_name', 'r') as file:
    final_content = file.read()
    print(final_content)

# Call the function to execute the program
file_operations()

# Answer Task 2
# Enter the initial content to write to the file: Hello, Pyth
# on!
# Initial content written to 'file_name'.
# Enter additional data to append to the file: Learning file 
# handling in python.
# Additional data appended to 'file_name'.

# Reading the final content of 'file_name':
# Hello, Python!
# Learning file handling in python.