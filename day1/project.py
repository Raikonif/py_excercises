# If the bill was $150.00, people between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇


def valditation_input(number):
    if float(number) > 0 and number.isdigit():
        return True
    else:
        return False


def tip_calculator(bill, people, tip=0.12):
    is_valid_bill = valditation_input(bill)
    is_valid_people = valditation_input(people)
    is_valid_tip = valditation_input(tip)

    if is_valid_bill and is_valid_people and is_valid_tip:
        bill_formatted = float(bill)
        tip_formatted = float(tip) / 100 + 1
        people = int(people)
        print(bill_formatted, tip_formatted)
        tip = (bill_formatted / people) * tip_formatted
        frmt_tip = "{:.2f}".format(tip)
        print(f"Tip: ${frmt_tip}")


tip_calculator(
    bill=input("Enter the bill: $\n"),
    people=input("Enter how many peoples do you want: \n"),
    tip=input("Enter the tip: \n")
)
