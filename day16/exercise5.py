# Exercise 5: Rectangle Class
# Create a class called Rectangle to represent a basic rectangle. The rectangle should have attributes for width and height.
# Add a method to calculate the area of the rectangle.
class Rectangle:
    def __init__ (self, ancho,largo):
        self.ancho = ancho
        self.largo = largo
    def __str__(self):
        return "Ancho:{}\nLargo:{}\n".format(self.ancho, self.largo)
rectangle = Rectangle("3","6")
print(rectangle)