# Unique Elements
# Write a program that takes a list of numbers as input and returns a new list containing only the unique elements from the original list.
# Do not use any built-in functions or libraries.

# Hints:
# Define a function called get_unique_elements(numbers) that takes a list of numbers as input
# and returns a new list containing only the unique elements.
# Use a for loop to iterate over the numbers and check if each element is already present in the new list before adding it.
def get_unique_elements(numbers):
    return set(numbers)
    numbers = numbers.repleace(" ", "")
    


numbers = input("Ingrese una lista de numeros para destacar entre ellos:\n")
resultado = get_unique_elements(numbers)
print(numbers)
print(resultado)