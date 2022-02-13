# Import statements

# Functions go here

# Checks that ticket name is not blank
def not_blank(question):
    valid=False
    while not valid:
        response=input(question)
        # If name is not blank, program continues
        if response !="":
            return response
        # If name is blank, show error (& repeat loop)
        else:
            print("Sorry - this can't be blank")

# ***** Main routine *****

# Set up dictionaires / lists to hold data

# Ask user if they have used the program before

# Loop to get ticket details

    # Get name (can't be blank)
    name = not_blank("Name: ")

    # Get age ( between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)

# Calculate total slaes and profit

# Output data to text file


