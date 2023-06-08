# Instructions
# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}",
# to format the 3 lists to be printed as a 3 by 3 square, each on a new line.
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# our job is to write a program that allows you to mark a square on the map using a two-digit system.
# The first digit in the input will specify the column (the position on the horizontal axis).
# The second digit in the input will specify the row number (the position on the vertical axis).
# So an input of 23 should place an X at the position shown below:

# Next, you need to use that input to update your nested list with an "x". Remember that your nested list map actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].
# Example Input 1
# column 2, row 3 would be entered as:

#         23
# Example Output 1
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']
# Example Input 2
# column 3, row 1 would be entered as:

#         31
# Example Output 2
# ['⬜️', '⬜️', 'X']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

filas= [
    ['⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬜️', '⬜️'],
    ]

fila1=[
 ['X', '⬜️', '⬜️'],

 ['⬜️', '⬜️', '⬜️'],

 ['⬜️', '⬜️', '⬜️'],
]

fila2=[
 ['⬜️', 'X', '⬜️'],

 ['⬜️', '⬜️', '⬜️'],

 ['⬜️', '⬜️', '⬜️'],
]

fila3=[
 ['⬜️', '⬜️', 'X'],

 ['⬜️', '⬜️', '⬜️'],

 ['⬜️', '⬜️', '⬜️'],
]

fila4=[
 ['⬜️', '⬜️', '⬜️'],

 ['X', '⬜️', '⬜️'],

 ['⬜️', '⬜️', '⬜️'],
]

fila5=[
 ['⬜️', '⬜️', '⬜️'],

 ['⬜️', 'X', '⬜️'],

 ['⬜️', '⬜️', '⬜️'],
]

fila6=[
 ['⬜️', '⬜️', '⬜️'],

 ['⬜️', '⬜️', 'X'],

 ['⬜️', '⬜️', '⬜️'],
]

fila7=[
 ['⬜️', '⬜️', '⬜️'],

 ['⬜️', '⬜️', '⬜️'],

 ['X', '⬜️', '⬜️'],
]

fila8=[
 ['⬜️', '⬜️', '⬜️'],

 ['⬜️', '⬜️', '⬜️'],

 ['⬜️', 'X', '⬜️'],
]

fila9=[
 ['⬜️', '⬜️', '⬜️'],

 ['⬜️', '⬜️', '⬜️'],

 ['⬜️', '⬜️', 'X'],
]

print(filas)

cua= input("Columna y fila:\n ")
if cua == "11":
    print(fila1)
elif cua == "12":
   print(fila2)
elif cua == "13":
    print(fila3)
elif cua == "21":
    print(fila4)
elif cua == "22":
    print(fila5)
elif cua == "23":
    print(fila6)
elif cua == "31":
    print(fila7)
elif cua == "32":
    print(fila8)
elif cua == "33":
    print(fila9)