import re

# Works out whether string has numbers and separates string into amount and item

test_strings=[
    "Popcorn",
    "2 pc",
    "1.5OJ",
    "4OJ",
]

for item in test_strings:
    # Regular expression to find if item starts with a number
    number_regex="^[1-9]"
    # If item has a number, separate it into two (number / item)
    if re.match(number_regex, item):
        amount=int(item[0])
        desired_snack=item[1:]
    else:
        amount=1
        desired_snack=item
    # Remove white space around snack
    desired_snack=desired_snack.strip()
    # If item does not have a number in front, set number to 1
    # Print order
    print("Amount:",amount)
    print("Snack: ",desired_snack)
    print("Length of snack:",len(desired_snack))