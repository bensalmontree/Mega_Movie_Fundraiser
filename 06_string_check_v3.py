# Function goes here
def string_check(choice,options):
    for var_list in options:
        # If the snack is in one of the lists, return the full function
        if choice in var_list:
            # Get full name of snack and put it in title case so it looks nice when outputted
            chosen=var_list[0].title()
            is_valid="yes"
            break
        # If the chosen option is not valid, set is_valid to no
        else:
            is_valid="no"
        # If the snack is not OK - ask questions again.
    if is_valid=="yes":
        return chosen
    else:
        return "invalid choice"

# Valid snacks holds list of all snacks
# Each item in valid snacks is a list with valid options for each snack <full name, letter code (a - e), and possible abbreviations etc>
valid_snacks=[
    ["popcorn","p","corn","a"],
    ["M&M's","m&m's","mms","m","b"],
    ["pita chips","chips","pc","pita","c"],
    ["water","w","d"]
]

yes_no=[
    ["yes","y"],
    ["no","n"]
]

check_snack="invalid choice"
while check_snack=="invalid choice":
    want_snack=input("Do you want to order snacks? ").lower()
    check_snack=string_check(want_snack,yes_no)

# Loop three times to make testing easier
for item in range(0,6):
    # Ask user for desired snack and put it in lowercase
    desired_snack=input("Snack: ").lower()
    # Check if snack is valid
    snack_choice=string_check(desired_snack,valid_snacks)
    print("Snack Choice: ",snack_choice)
