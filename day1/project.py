# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇


def valditation_input(bill):
    if float(bill) > 0 and bill.isdigit():
        return True
    else:
        return False


def tip_calculator(bill, split):
    is_valid_bill = valditation_input(bill)
    is_valid_split = valditation_input(split)
    if is_valid_bill and is_valid_split:
        bill_formatted = float(bill)
        tip = (bill_formatted / 5) * 1.12
        frmt_tip = "{:.2f}".format(tip)
        print(f"Tip: ${frmt_tip}")


tip_calculator(
    input("Enter the bill: $\n"), input("Enter how many splits do you want: \n")
)
