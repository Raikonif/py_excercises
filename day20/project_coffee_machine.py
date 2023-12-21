# coffee machine project
# 1. print a report
# 2. check resources sufficient
# 3. process coins
# 4. check transaction successful
# 5. make coffee

WATER = "water"
MILK = "milk"
COFFEE = "coffee"

EXPRESSO = "expresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"

resources = {
    WATER: 3000,
    MILK: 2000,
    COFFEE: 1000,
}

menu = {
    EXPRESSO: {
        "ingredients": {
            WATER: 50,
            MILK: 0,
            COFFEE: 18,
        },
        "cost": 1.5,
    },
    LATTE: {
        "ingredients": {
            WATER: 200,
            MILK: 150,
            COFFEE: 24,
        },
        "cost": 2.5,
    },
    CAPPUCCINO: {
        "ingredients": {
            WATER: 250,
            MILK: 100,
            COFFEE: 24,
        },
        "cost": 3.0,
    },
}


def print_report():
    for key, value in resources.items():
        print(f"{key}: {value}")


def client_product_request(user_input_request):
    water_requirement = menu[user_input_request]["ingredients"][WATER]
    milk_requirement = menu[user_input_request]["ingredients"][MILK]
    coffee_requirement = menu[user_input_request]["ingredients"][COFFEE]
    if (
        water_requirement <= resources[WATER]
        and milk_requirement <= resources[MILK]
        and coffee_requirement <= resources[COFFEE]
    ):
        print("resources enough")
        return True
    else:
        print("insufficent resources")
        return False


def client_payment_done(total):
    if total <= 1.5:
        return False
    else:
        return True


def client_payment_counter(quarters, dimes, nickles, pinnies):
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pinnies * 0.01)


def process_coins():
    quarters = float(input("how many quarters do you put? "))
    dimes = float(input("how many dimes do you put? "))
    nickles = float(input("how many nickles do you put? "))
    pinnies = float(input("how many pinnies do you put? "))
    total = client_payment_counter(quarters, dimes, nickles, pinnies)
    is_done = client_payment_done(total)
    return total, is_done


def is_valid_option(input_user):
    if input_user == 1 or input_user == 2 or input_user == 3 or input_user == 4:
        return True
    else:
        return False


def what_option_is(input_user):
    if input_user == 1:
        return EXPRESSO
    elif input_user == 2:
        return LATTE
    elif input_user == 3:
        return CAPPUCCINO
    elif input_user == 4:
        print("Good Bye!!")
        return


def coffee_machine(user_input_request):
    is_true = True
    if is_valid_option(user_input_request):
        option = what_option_is(user_input_request)
        can_make_that_coffee = client_product_request(option)
        if not can_make_that_coffee:
            return "Cannot make your Coffee, there is not resources enough"
        while is_true:
            total, correct_payment = process_coins()
            if not correct_payment:
                print(f"total: {total}, Insufficent payment for your coffe")
            else:
                is_true = False
        if can_make_that_coffee and correct_payment:
            return "Making Coffe... 3, 2, 1, Done!.."


docstringmachine = """
COFFEE MACHINE:
WANNA A CUP OF COFFEE?
SELECT ONE OF THE NEXT OPTIONS:
1. EXPRESSO
2. LATTE
3. CAPPUCCINO
4. QUIT
"""
print_report()
print(coffee_machine(int(input(docstringmachine))))
