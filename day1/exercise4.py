# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# Hint
# 1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# 2. Try copying the example output into your code and replacing the relevant parts so that the sentence is formated the same way.
fecha= input("Ingrese fecha de nacimiento (dd/mm/yyyy): ")

try:
    from datetime import datetime
    fecha= datetime.steptime(fecha, '%d/%m/y')
except:
    print("La fecha integrada no es correcta, debe ser : (dd/mm/yyyy)")
    exit ()

anio = fecha.year
mes = fecha.month
dia = fecha.day

fechaH = datetime.today()
anioH = fechaH.year
mesH = fechaH.month
diaH = fechaH.day

mesAdicional = 0
if (dia > diaH):
    import calendar
    ultimoDia = calendar.monthrange (mes, mesH)[1]
    diaH = diaH + ultimoDia
    mesAdicional = 1

dias = diaH - dia

anioAdicional = 0
if (mes > mesH):
    mesH = mesH +12
    anioAdicional = 1

meses = mesH - (mes + mesAdicional)
anios = anioH - ( anio + anioAdicional)

print(str(anios)+"Años"+str(meses)+"Meses"+str(dias)+ "Dias")