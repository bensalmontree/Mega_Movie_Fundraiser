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

# Checks for an integer between two values
def int_check(question, low_num, high_num):
    error="Please enter a whole number between {} and {}".format(low_num, high_num)
    valid = False
    while not valid:
        try:
            response=int(input(question))
            if low_num<=response<=high_num:
                return response
            else:
                print(error)
        except ValueError:
            print(error)
            
# ***** Main routine *****

# Set up dictionaires / lists to hold data

# Ask user if they have used the program before

# Loop to get ticket details
# Initialise loop so that it runs at least once
name=""
count=0
MAX_TICKETS=5

while name!="xxx" and count<MAX_TICKETS:
    # Tells user how many seats are left
    if count<4:
        print("You have {} seats left".format(MAX_TICKETS - count))
    # Warns user that only one seat is left
    else:
        print("There is only ONE seat left")
    # Get details...
    # Get name (can't be blank)
    name=not_blank("Name: ")
    if name=="xxx":
        break
    count+=1
    
    # Get age (between 12 and 130)
    age=int_check("Age:",12,130)

if count==MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. There are {} places still available".format(count, MAX_TICKETS - count))

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)

# Calculate total slaes and profit

# Output data to text file


