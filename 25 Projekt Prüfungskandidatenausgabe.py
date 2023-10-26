# Anforderung Lehrer: Programm dass Leute zur Wiederholung dran nimmt
# 3 Leute zur Wiederholung dürfen nicht immer die gleichen sein
# 2 bis 3 Rollen (Programmierer, Person die Anforderungen einholt und Programmierer
# brieft, Person die recherchiert)
# students wiederholen sich leider

import random

# List of all student names
all_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

# Use a set to store available students
# The line available_students = set(all_students) in Python creates a new set
# named available_students and populates it with the elements from the list
# all_students

available_students = set(all_students)

# List to store selected students
selected_students = []

# Number of students to select
num_students_to_select = 3

# Check if there are enough students
if len(all_students) >= num_students_to_select:
    for _ in range(num_students_to_select):
        # Randomly select a student from available students
        student = random.choice(list(available_students))

        # Remove the selected student from the available students
        available_students.remove(student)

        # Add the selected student to the list of selected students
        selected_students.append(student)

    # Print the selected students
    print("Selected students for the exam:")
    for student in selected_students:
        print(student)
else:
    print("There are not enough students to select from.")