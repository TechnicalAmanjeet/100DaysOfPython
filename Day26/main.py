# ********** List comprehension challenge **********

# challange 1.
import random

string = "Amanjeet"
new_list = [alphabet for alphabet in string]
print(len(new_list))

# challange 2
new_list = [number * 2 for number in range(0, 11)]
# print(new_list)

# challenge 3.
names = ["Amanjeet", "Kajal", "Riya", "Neha", "abp", "kismat", "Anjali", "a", "b"]

new_names_list = [name.upper() for name in names if len(name) > 3]
# print(new_names_list)


# ******** Dict comprehension challenge *********

# Challenge 1
students = ["Amanjeet", "Kajal", "Riya", "Neha", "abp", "kismat", "Anjali"]

students_score_card = {student: random.randint(0, 100) for student in students}
print(students_score_card)

# challenge 2
passed_students = [student for (student, student_score) in students_score_card.items() if student_score >= 60]
print(passed_students)

passed_students_dict = {student: student_score for (student, student_score) in students_score_card.items() if
                        student_score >= 60}
print(passed_students_dict)

# for (student, score) in students_score_card.items():
#     print(f"{student} : {score}")
