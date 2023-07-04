# Exercise 1: Student Class
# Create a class called Student to represent a basic student.
# The student should have attributes like name, age, and a list of grades.
# Add methods to calculate the average grade and display the student's information.
# Hint
# Use the following code to test your class:
# student = Student("Angela", 12)
# student.add_grade(grade=75)
# student.add_grade(grade=87)
# student.add_grade(grade=65)
# print(student.get_average_grade())
# print(student.name)
# print(student.age)
# print(student.grades)
# Example Output
# 75.66666666666667
# Angela
# 12
# [75, 87, 65]
lista= [75,87,65]
a = 75
b = 87
c = 65
promedio= (75+87+65)/3
print(promedio)
class Student:
    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades
Angela = Student("Angela", "12", lista)
print (Angela)
