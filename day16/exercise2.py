# Exercise 2: Car Class
# Create a class called Car to represent a basic car.
# The car should have attributes like make, model, and year. Add a method to display the car's information.
class Car:
     def __init__ (self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
Toyota = Car("Toyota","Modelo 3","2012")
print(Toyota.marca, Toyota.modelo, Toyota.anio)