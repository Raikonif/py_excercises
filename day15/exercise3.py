# Exercise 3: Dog Class
# Create a class called Dog to represent a basic dog.
# It should have attributes like name and age. Add methods to make the dog bark and display its information.
class Dog:
    def __init__(self, nombre, raza, edad,color):
     self.nombre=  nombre
     self.raza = raza
     self.edad = edad
     self.color = color
    
    def __str__(self):
        return "Nombre:{}\nRaza:{}\nEdad:{}\nColor:{}\n".format(self.nombre, self.raza, self.edad,self.color)

Razzia = Dog("Razzia", "Criollo","7","Negro")
print(Razzia)