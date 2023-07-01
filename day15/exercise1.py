# Sure! Here are three basic exercises to practice Object-Oriented Programming (OOP) concepts in Python:

# Exercise 1: Creating a Class
# Create a class called Person that represents a basic person with attributes such as name, age, and gender.
# Add a method to print the person's information.
class Persona:
    def __init__(self,nombre,apellidos,edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    def __str__(self):
        return "Nombre:{}\nApellidos:{}\nEdad:{}".format(self.nombre, self.apellidos, self.edad)

Diego = Persona("Diego", "Alarcon Inturias","31")
print(Diego)