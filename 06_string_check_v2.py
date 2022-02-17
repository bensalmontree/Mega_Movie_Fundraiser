# Functions go here

# String checking functiions, takes in question and list of valid responses
import string

def string_check(question,to_check):
    valid=False 
    while not valid:
        response=input(question).lower()
        if response in to_check:
            return response
        else:
            for item in to_check:
                # Checks if response is the first letter of an item in th list
                if response==item[0]:
                    # Note: returns the entire response rather than just the letter
                    return item
        print("Sorry that is not a valid response\n")
            
# Each item in valid snacks is a list with valid options for each snack <full name, letter code (a - e), and possible abbreviations etc>
valid_snacks=[
    ["popcorn","p","corn","a"],
    ["M&M's","m&m's","mms","m","b"],
    ["pita chips","chips","pc","pita","c"],
    ["water","w","d"]
]

# Initialise variables
snack_ok=""
snack=""

# Loop three times to make testing quicker
for item in range(0,3):
    # Ask user for desired snack and put it in lowercase
    desired_snack=input("Snack: ").lower()
    for var_list in valid_snacks:
        # If the snack is in one of the lists, return the full name
        if desired_snack in var_list:
            # Get full name of snack and put it in title case so it looks nice when outputted
            snack=var_list[0].title()
            snack_ok="yes"
            break
        # If the chosen snack is not valid, set snack_ok to no
        else:
            snack_ok="no"
    # If the snack is not OK - ask questions again.
    if snack_ok=="yes":
        print("Snack Choice: ",snack)
    else:
        print("Invalid choice")
