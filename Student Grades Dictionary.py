# -------------------------------
# Problem 1: Student Grades Dictionary
# -------------------------------
# Given a list of tuples containing student names and their scores:
# students = [("Asha", 88), ("Ravi", 92), ("Meena", 79), ("Arjun", 88)]
#
# 1. Create a dictionary called 'student_scores' where:
#       - key = student name
#       - value = score
# 2. Print all students who have a score above 80.
# 3. Add a new student "Tina" with a score of 95.
# -------------------------------

students = [("Asha", 88), ("Ravi", 92), ("Meena", 79), ("Arjun", 88)]

# using dictionary comprehension 

student = {name: score for name, score in students}
student_above_80 = [x for name, x in students if x > 80]
print(student_above_80)
student["Tina"] = 95
print(student)



