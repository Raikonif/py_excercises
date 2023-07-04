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


print(
    """
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
"""
)

coordinates = input("put two digits number between 1 to 3:\n")
if (
    0 < int(coordinates[0]) <= 3
    and 0 < int(coordinates[1]) <= 3
    and len(coordinates) == 2
):
    row = int(coordinates[0])
    column = int(coordinates[1])

    map = [["⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️"]]
    map[row - 1][column - 1] = "X"

    print(f"{map[0]}\n{map[1]}\n{map[2]}")
else:
    print("please enter two digits number between 1 to 3")
