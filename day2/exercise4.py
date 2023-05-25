# Instructions
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


def prices_products(product):
    switcher_price_products = {
        "S": 15,
        "M": 20,
        "L": 25,
        "PS": 2,
        "PM": 3,
        "PL": 3,
        "C": 1,
    }
    return switcher_price_products.get(product, "Doesn't Exist")


def input_validation(input_data):
    try:
        if (
            prices_products(input_data) != "Doesn't Exist"
            or input_data == "Y"
            or input_data == "N"
        ):
            return True
    except ValueError:
        return False


def make_order(pizza_order, add_pepperoni, extra_cheese):
    is_valid_pizza = input_validation(pizza_order)
    is_valid_pepperoni = input_validation(add_pepperoni)
    is_valid_cheese = input_validation(extra_cheese)
    if is_valid_pizza and is_valid_pepperoni and is_valid_cheese:
        total = prices_products(pizza_order)
        if add_pepperoni == "Y":
            total += prices_products(f"P{pizza_order}")
        if extra_cheese == "Y":
            total += prices_products("C")
        return f"The total Bill is ${total}"
    else:
        return "Invalid Input"


print(
    """Please Create Your Order:
We have Pizzas with different size and prices
Small Pizza (S): $15
Medium Pizza (M): $20
Large Pizza (L): $25
+ Pepperoni: (S) $2
+ Pepperoni: (M, L) $2
Extra Cheese: $1"""
)
order = make_order(
    input("Select The size of your Pizza 'S, M, L':\n"),
    input("Wanna Add Pepperoni? 'Y/N':\n"),
    input("Wanna Extra Cheese? 'Y/N':\n"),
)
print(f"Your total bill is ${order}")
