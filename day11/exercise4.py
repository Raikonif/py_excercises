# Access Global Variable
# Instructions
# Write a function called "access_global_variable" that does not take any input.
# Access a global variable inside the function and print its value.
# Then, assign a new value to the global variable. Finally, ask the user to enter a number, call the function,
# and print the updated global variable.
hermanito = 1 + 10
hermanitu = 10 + 10
def access_global_variable():
    print(hermanito)
usuario = input("Ingrese (1) or (2) para la sorpresa:")
if usuario == "1":
    print(hermanito)
elif usuario == "2":
    print(hermanitu)