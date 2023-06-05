# Instructions
# You are going to write a program that calculates the average student height from a List of heights.

# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

# e.g.

# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

# There are a total of 7 heights in student_heights

# 1146 ÷ 7 = 163.71428571428572

# Average height rounded to the nearest whole number = 164

# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

# Example Output
# 171
# Hint
# Remember to use the round() function to round the average height before you print it.
number = input ("Ingrese la cantidad de personas: ")
if number > 1:
    altura_hombres = 0
    altura_mujeres = 0
    cantidad_hombres = 0
    cantidad_mujeres = 0

    for datos in range(n):
        
        altura = int(input("Ingrese la altura en Cm: "))
        genero = input("Ingrese el genero de la persona (M) (H): ")

        if genero.upper() == "M":
            altura_M += altura
        
        elif genero.upper() == "H":
            altura_H += altura
        else:
            print("Genero seleccionado incorrecto")

    promedio = altura_M / cantidad_mujeres
    promedio2 = altura_H / cantidad_hombres

    print("De acuerdo a los datos los promedios son:")
    print("Promedio altura H = Hombres:", promedio2)
    print("Promedio altura M = Mujeres:", promedio)

else:
    print("Ingreso incorrectamente, intentelo nuevamente")