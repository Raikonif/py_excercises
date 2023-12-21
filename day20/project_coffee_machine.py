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
