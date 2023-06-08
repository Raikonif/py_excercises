# Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.

# You've been to Moscow and Saint Petersburg.

# DO NOT modify the travel_log directly. You need to create a function that modifies it.

# Hint
# Look at the function call above to see what the name of the function should be.

# The inputs for the function are positional arguments. The order is very important.

# Feel free to choose your own parameter names.
add_new_country=([
    'Russia' , '2',
    "Moscow" , "1",
    "Saint Petersburg", "1"
    ])
country = input("Ingrese A para saber cuantas veces has estado en Russia y B en que lugares mas visitaste:\n")
if country == "A":
    print("Visitaste Russia:")
    print(add_new_country["Russia"], veces)
elif country == "B":
    print("Estuviste en estos lugares mas:")
    print(add_new_country)

