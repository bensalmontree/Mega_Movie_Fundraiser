# Import statements

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
            
# ***** Main routine *****

# Set up dictionaries / lists to hold data

# Ask user if they have used the program before

# Loop to get ticket details
# Start of loop
# Initialise loop so that it runs at least once
MAX_TICKETS=5
name=""
ticket_count=0
ticket_sales=0


while name!="xxx" and ticket_count<MAX_TICKETS:
    # Tells user how many seats are left
    if ticket_count<MAX_TICKETS-1:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))
    # Warns user that only one seat is left
    else:
        print("There is only ONE seat left")
    # Get details...
    # Get name (can't be blank)
    name=not_blank("Name: ")
    if name=="xxx":
        break
    # Get age (between 12 and 130)
    age=int_check("Age: ")
    # Check that age is valid...
    if age<12:
        print("Sorry you are too young for this movie")
        continue
    elif age>130:
        print("That is very old - it looks like a mistake")
        continue
    if age<16:
        ticket_price=7.5
    elif age<65:
        ticket_price=10.5
    else:
        ticket_price=6.5
    ticket_count+=1
    ticket_sales+=ticket_price

# End of tickets loop
# Calculate ticket profit...
ticket_profit=ticket_sales-(5*ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

if ticket_count==MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text file

