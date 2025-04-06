'''
Task 1: Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''

student_marks = {
    'John Doe'      : 85,
    'Jane Smith'    : 92,
    'Alice Johnson' : 78,
    'Bob Brown'     : 95
}

def get_student_marks(student_marks, student_name):
    if student_name in student_marks:
        return f'Marks for {student_name}: {student_marks[student_name]}'
    else:
        return 'Student not found in the dictionary.'

student_name = input('Enter a student name: ')
print(get_student_marks(student_marks, student_name))