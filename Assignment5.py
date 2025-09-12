# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

# students_marks= {'Aksa': 80, 'Ruba': 75, 'Alex': 62, 'Kevin': 54}

# students_name= input ("Enter a student's name:")
# if students_name in students_marks:
#     marks= students_marks[students_name]
#     print (f"{students_name} marks:{marks}")
# else:
#     print (f"student not found") 
# Condition 1:
# Enter a student's name:Aksa
# Aksa marks:80

# Condition 2:
# Enter a student's name:Radha
# student not found

# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

# 1. Creates a list of numbers from 1 to 10.
number = list(range(1,11))
# 2. Extracts the first five elements from the list.
extracted_file = number[0:5 ]
# 3. Reverses these extracted elements.
reversed_file = extracted_file[::-1]

print (f"Original list:",number)
print (f"Extacted first five elements:",extracted_file)
print (f"Reversed extracted elements:",reversed_file)

# Answer Task 2:
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Extacted first five elements: [1, 2, 3, 4, 5]
# Reversed extracted elements: [5, 4, 3, 2, 1]

