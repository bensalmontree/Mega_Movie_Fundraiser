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
        print("Please enter a valid option")
        return "invalid choice"

def instructions(options):
    show_help="invalid choice"
    while show_help=="invalid choice":
        show_help=input("Would you like to read the instructions? ")
        show_help=string_check(show_help,options)
    
    if show_help=="yes":
        print()
        print("**** Mega Movie Fundraiser Instructions ****")
        print()
        print("Instructions go hre. They are brief and helpful").lower()

    return ""


# Main Routine goes here
# List for valid yes / no responses
yes_no=[
    ["yes","y"],
    ["no","n"]
]

# Ask if instructions are needed
instructions(yes_no)
print()
print("Program launches...")