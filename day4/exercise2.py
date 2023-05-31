# Instructions
# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x

# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

# Example Output
# The highest score in the class is: 91

# Hint
# Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?
n = int(input("Ingrese sus calificaciones: "))
calificacion_alta = 0

for n in range(10):
    n = int(input(f"Ingrese {n+1} califiacion: "))
    if calificacion_alta < n:
        calificacion_alta = n
print("La calificacion mas alta es:{}.format{calificacion_alta}")
