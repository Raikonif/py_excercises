#Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

# Hint
# 1. Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.
usuario = input ("Tamaño de pizza (P=Pequeña) (M= Mediana) (G=Grande):\n ")
p = 15
m = 20
g = 25

if usuario == "P":
    print("cuenta$:",p)
elif usuario == "M":
    print("cuenta$:", m)
elif usuario == "G":
    print("cuenta$:", g)
else:
    ("Incorrecto, seleccione nuevamente")

usuario1 = input("Con peperoni (Y= Yes) (N=No):\n")
pp1= p+2
pp2= 20+3
pp3= 25+3
suma = usuario + pp1
suma1 = usuario + pp2
suma2= usuario +pp3
if usuario1 == "Y":
        if usuario1 == p:
            print(suma)
        else:
            print(suma1)
            print(suma2)

elif usuario1 == "N":
    print("Total",usuario)

usuario2 = input("Desea Queso extra? (Y=Yes) (N=No):\n")
sumaa = usuario + 1
sumab = usuario+usuario1+usuario2
if usuario2 == "Y":
    print(sumaa)
elif usuario == "N":
    print(sumab)
else:
    print("Incorrecto")
    