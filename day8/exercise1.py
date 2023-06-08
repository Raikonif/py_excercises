# Instructions
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

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
print("Bienvenidos!!, estan listos para ver notas? :)")
student_scores = {
    'Harry': '90', 
    'Ron': '71', 
    'Hermione': '100', 
    'Draco': '80', 
    'Neville': '70'
    }
student_grades = {
    'Harry': 'Exceeds Expectations', 
    'Ron': 'Acceptable', 
    'Hermione': 'Outstanding', 
    'Draco': 'Acceptable', 
    'Neville': 'Fail'
    }

for ellos in student_scores:
    print( ellos)

student = input("Ingrese su nombre para ver su calificacion:\n")
if student == "Harry":
    print("Tu calificaion fue:")
    print(student_grades['Harry'])
elif student == "Ron":
    print("Tu calificaion fue:")
    print(student_grades['Ron'])
elif student == "Hermione":
    print("Tu calificaion fue:")
    print(student_grades['Hermione'])
elif student == "Draco":
    print("Tu calificaion fue:")
    print(student_grades['Draco'])
elif student == "Neville":
    print("Tu calificaion fue:")
    print(student_grades['Neville'])
else:
    print("INCORRECTO, Escriba bien su nombre(No se olvide mayus. al principio de su nombre)")
