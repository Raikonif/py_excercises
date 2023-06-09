# create a calculator that can +, -, *, / between 2 or more numbers
# make a variable validation function to know if the input is a valid number

# e.g:

# operation *
# inputs 1 , 4, 5
# output 20

# operation -
# inputs 2, 4, 6, 2
# output -10

# operation /
# inputs 2,2
# output 1
number = input("Ingrese el primer numero:")
number1 = input("Ingrese el segundo numero:")
number2 = input("Ingrese el segundo numero:")
number3 = input("Ingrese el segundo numero:") 

suma = number + number1
suma1 = number + number1 + number2
suma2 = number + number1 + number2 + number3
resta = number - number1
resta1 = number - number1 - number2
resta2 = number - number1 - number2 - number3
multi = number * number1
multi1 = number * number1 * number2
multi2 = number * number1 * number2 * number3
divi = number / number1
divi1 = number / number1 / number2
divi2 = number / number1 / number2 / number3


eleccion = 0

while eleccion != 6:
    print("""
    Ingrese la operaion a realizar
    1) SUMA
    2) RESTA
    3) MULTIPLICACION
    4) DIVISION
    5) SALIR
    """)
    
    eleccion = int(input())


 

if eleccion == 1:
    print("Ingrese de cuantos numeros: ")
    sel = input("2,3,4 numeros: ")
    if sel == "2":
        print(number)
        print(number1)
        print("Resultado:", suma)
    elif sel == "3":
        print(number)
        print(number1)
        print(number2)
        print("Resultado:", suma1)
    elif sel == "4":
        print(number)
        print(number1)
        print(number2)
        print(number3)
        print("Resultado:", suma2)
elif eleccion == 2:
    print("Ingrese de cuantos numeros: ")
    sel = input("2,3,4 numeros: ")
    if sel == "2":
        print(number)
        print(number1)
        print("Resultado:", resta)
    elif sel == "3":
        print(number)
        print(number1)
        print(number2)
        print("Resultado:", resta1)
    elif sel == "4":
        print(number)
        print(number1)
        print(number2)
        print(number3)
        print("Resultado:", resta2)
elif eleccion == 3:
    print("Ingrese de cuantos numeros: ")
    sel = input("2,3,4 numeros: ")
    if sel == "2":
        print(number)
        print(number1)
        print("Resultado:", multi)
    elif sel == "3":
        print(number)
        print(number1)
        print(number2)
        print("Resultado:", multi1)
    elif sel == "4":
        print(number)
        print(number1)
        print(number2)
        print(number3)
        print("Resultado:", multi2)
elif eleccion == 4:
    print("Ingrese de cuantos numeros: ")
    sel = input("2,3,4 numeros: ")
    if sel == "2":
        print(number)
        print(number1)
        print("Resultado:", divi)
    elif sel == "3":
        print(number)
        print(number1)
        print(number2)
        print("Resultado:", divi1)
    elif sel == "4":
        print(number)
        print(number1)
        print(number2)
        print(number3)
        print("Resultado:", divi2)
elif eleccion == 5:
        print("Hasta pronto!!")
      





