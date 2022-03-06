import re

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
        print("Please enter a valid option")
        return "invalid choice"

# Gets list of snacks
def get_snack():
    # regular expression to find if item starts with a number
    number_regex="^[1-9]"

    # Valid snacks holds list of all snacks
    # Each item in valid snacks is a list with valid options for each snack <full name, letter code (a - e), and possible abbreviations etc>
    valid_snacks=[
        ["popcorn","p","corn","a"],
        ["M&M's","m&m's","mms","m","b"],
        ["pita chips","chips","pc","pita","c"],
        ["water","w","d"],
        ["orange juice","oj","o","juice","e"]
    ]

    # Holds snack order for a single user
    snack_order=[]

    desired_snack=""
    while desired_snack!="xxx":
        snack_row=[]
        # Ask user for desired snack and put it in lowercase
        desired_snack=input("Snack: ").lower()
        # Break code
        if desired_snack=="xxx":
            return snack_order
        # If item has a number, seperate it into two 
        if re.match(number_regex,desired_snack):
            amount=int(desired_snack[0])
            desired_snack=desired_snack[1:]
        else:
            amount=1
            desired_snack=desired_snack
        # Remove white space around snack
        desired_snack=desired_snack.strip()
        # Check if snack is valid
        snack_choice=string_check(desired_snack,valid_snacks)
        # Check snack amount is valid (less than 5)
        if amount>=5:
            print("Sorry - we have a four snack maximum")
            snack_choice="invalid choice"
        # Add snack AND amount to list...
        snack_row.append(amount)
        snack_row.append(snack_choice)
        # Check that snack is not the exit code before adding
        if snack_choice!="xxx"and snack_choice!="invalid choice":
            snack_order.append(snack_row)

# Valid options for yes / no questions
yes_no=[
    ["yes","y"],
    ["no","n"]
]

# Ask user if they want a snack
check_snack="invalid choice"
while check_snack=="invalid choice":
    want_snack=input("Do you want to order snacks? ").lower()
    check_snack=string_check(want_snack,yes_no)

# If they say yes, ask what snacks they want (and add to our snack_list)
if check_snack=="Yes":
    get_order=get_snack()
else:
    get_order=[]

# Show snack orders
print()
if len(get_order)==0:
    print("Snack Ordered: None")
else:
    print("Snacks Ordered:")
    '''for item in snack_order:
        print(item)'''
    print(get_order)

