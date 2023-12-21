# Instructions
# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.
# The final version of the student_grades dictionary will be checked.

# DO NOT modify lines 1-7 to change the existing student_scores dictionary.

# DO NOT write any print statements.

# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"

# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
# Hint
# Remember that looping through a Dictionary will only give you the keys and not the values.

# If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.

# At the end of your program, the print statement will show the final student_scores dictionary, do not change this.

students_scores = [
    {"name": "Harry Potter", "score": 81},
    {"name": "Ron Weasley", "score": 78},
    {"name": "Hermione Granger", "score": 99},
    {"name": "Draco Malfoy", "score": 74},
    {"name": "Neville Longbottom", "score": 62},
]

students_grades = []


def convert_scores_to_grades():
    for student in students_scores:
        current_student_grade = {}
        current_student_grade["name"] = student["name"].split()[0]
        if student["score"] > 90:
            current_student_grade["score"] = "Outstanding"
        elif student["score"] > 80:
            current_student_grade["score"] = "Exceeds Expectations"
        elif student["score"] > 70:
            current_student_grade["score"] = "Acceptable"
        else:
            current_student_grade["score"] = "Fail"
        students_grades.append(current_student_grade)


convert_scores_to_grades()
print(students_grades)
