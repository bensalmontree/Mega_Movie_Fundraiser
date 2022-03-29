# Import statements
import re
import pandas

# Functions go here

# Checks that ticket name is not blank
def not_blank(question):
    valid=False
    while not valid:
        response=input(question)
        # If name is not blank, program continues
        if response!="":
            return response
        # If name is blank, show error (& repeat loop)
        else:
            print("Sorry - this can't be blank")

# Checks for an integer more than 0
def int_check(question):
    error="Please enter a whole number that is more than 0"
    valid=False
    while not valid:
        # Ask user for number and check it is valid
        try:
            response=int(input(question))
            if response<=0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)
            
# Checks number of tickets left and warns user if maxium is being approached
def check_tickets(tickets_sold,ticket_limit):
    # Tells user how many seats are left
    if tickets_sold<ticket_limit-1:
        print("You have {} seats left".format(ticket_limit-tickets_sold))
    # Warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")
    return""

# Gets ticket price based on age
def get_ticket_price():
    # Get age (between 12 and 130)
    age=int_check("Age: ")
    # Check that age is valid...
    if age<12:
        print("Sorry you are too young for this movie")
        return"invalid ticket price"
    elif age>130:
        print("That is very old - it looks like a mistake")
        return"invalid ticket price"
    if age<16:
        ticket_price=7.5
    elif age<65:
        ticket_price=10.5
    else:
        ticket_price=6.5

    return ticket_price

# WARNING: The response is returned in title case
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

def get_order():
    # regular expression to find if item starts with a number
    number_regex="^[1-9]"

    # Valid snacks holds list of all snacks
    # Each item in valid snacks is a list with valid options for each snack <full name, letter code (a - e), and possible abbreviations etc>
    valid_snacks=[
        ["popcorn","p","corn","a"],
        ["MMs", "M&M's","m&m's","mms","m","b"],
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

# ***** Main routine *****

# Set up dictionaires / lists to hold data

# List of valid yes / no responses
yes_no=[
    ["yes","y"],
    ["no","n"]
]

# List of valid responses for payment method
pay_method=[
    ["cash","ca"],
    ["credit","cr"]
]

# Initialise loop so that it runs at least once
MAX_TICKETS=5
name=""
ticket_count=0
ticket_sales=0

# Initailise lists (to make data-fram in due course)
all_names=[]
all_tickets=[]
popcorn=[]
mms=[]
pita_chips=[]
water=[]
orange_juice=[]

snack_lists=[popcorn,mms,pita_chips,water,orange_juice]

# Store surcharge multiplier
surcharge_mult_list=[]

# Lists to store summary data...
summary_headings=["Popcorn","Mms","Pita Chips","Water","Orange Juice","Snack Profit","Ticket Price","Total Profit"]

summary_data=[]

# Data Frame Dictionary
movie_data_dict={
    'Name':all_names,
    'Popcorn':popcorn,
    'Water':water,
    'Pita Chips':pita_chips,
    'Mms':mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier':surcharge_mult_list, 
    'Ticket': all_tickets
}

# Summary Dictionary
summary_data_dict={
    'Item':summary_headings,
    'Amount':summary_data
}

# Cost of each snack
price_dict={
    'Popcorn':2.5,
    'Water':2,
    'Pita Chips':4.5,
    'Mms':3,
    'Orange Juice':3.25
}

# Ask user if they have used the program before & show instructions

# Loop to get ticket details
while name!="xxx"and ticket_count<MAX_TICKETS:
    # Check numbers of ticket limit has not been exceeded...
    check_tickets(ticket_count,MAX_TICKETS)
    
    # **** Get details for each tickets... ****

    # Get name (can't be blank)
    name=not_blank("Name: ")

    # End the loop if the exit code is entered
    if name=="xxx":
        break

    # Get ticket price based on age
    ticket_price=get_ticket_price()
    # If age is invalid, restart loop (and get name again)
    if ticket_price=="invalid ticket price":
        continue

    ticket_count+=1
    ticket_sales+=ticket_price

    # add name and ticket price to list
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Ask user if they want a snack
    check_snack="invalid choice"
    while check_snack=="invalid choice":
        want_snack=input("Do you want to order snacks? ").lower()
        check_snack=string_check(want_snack,yes_no)

    # If they say yes, ask what snacks they want
    if check_snack=="Yes":
        snack_order=get_order()
    else:
        snack_order=[]

    # Assume no snacks have been bought
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item)>0:
            to_find=(item[1])
            amount=(item[0])
            add_list=movie_data_dict[to_find]
            add_list[-1]=amount

    # Get payment method (ie: work out if surcharge is needed) 
    # Ask for payment method
    how_pay="invalid choice"
    while how_pay=="invalid choice":
        how_pay=input("Please choose a payment method (cash or credit): ")
        how_pay=string_check(how_pay,pay_method)
    
    if how_pay=="Credit":
        surcharge_multiplier=0.05
    else:
        surcharge_multiplier=0
    
    surcharge_mult_list.append(surcharge_multiplier)


# End of tickets / snacks / payment loop

# Create dataframe and get index to name column
movie_frame=pandas.DataFrame(movie_data_dict)

movie_frame=movie_frame.set_index('Name')

# Create column called 'Sub Total'
# fill it price for snacks and ticket
movie_frame["Snacks"]=\
    movie_frame['Ticket']+\
    movie_frame['Popcorn']*price_dict['Popcorn']+\
    movie_frame['Water']*price_dict['Water']+\
    movie_frame['Pita Chips']*price_dict['Pita Chips']+\
    movie_frame['Mms']*price_dict['Mms']+\
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Sub Total"]=\
    movie_frame['Ticket']+\
    movie_frame['Snacks']


movie_frame["Surcharge"]=\
    movie_frame["Sub Total"]*movie_frame["Surcharge_Multiplier"]



movie_frame["Total"]=movie_frame["Sub Total"]+\
    movie_frame['Surcharge']



# movie_frame=movie_frame.reindex(columns=['Sub Total','Ticket','Name','Popcorn','Water','Pita Chips','Mms','Orange Juice','Surcharge_multiplier'])

# Shorten column names
movie_frame=movie_frame.rename(columns={'Orange Juice':'OJ','Pita Chips':'Chips','Surcharge_Multiplier':'SM'})

# Set up summary dataframe
# populate snack ideas...
for item in snack_lists:
    # sum ideas in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total=movie_frame['Snack'].sum()
snack_profit=snack_total*0.2
summary_data.append(snack_profit)

# Get Ticket profit and add to list
ticket_profit=ticket_sales=(5*ticket_count)
summary_data.append(ticket_profit)

# Work out total profit and add to list
total_profit=snack_profit+ticket_profit
summary_data.append(total_profit)

# Set up columns to be printed...
pandas.set_option('display.max_columns', None)

# Display numbers to 2 dp...
pandas.set_option('precision', 2)

print_all=input("Print all columns?? (y) for yes ")
if print_all=="y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket','Sub Total','Surcharge','Total']])

print()

# Calculate ticket profits...
ticket_profit=ticket_sales-(5*ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets
if ticket_count==MAX_TICKETS:
    print("You have sold all the available tickets!")

