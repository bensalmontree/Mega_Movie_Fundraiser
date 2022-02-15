# Function goes here

# Checks for an integer more than 0
def int_check(question):
    error="Please enter a whole number that is more than 0"
    valid=False
    while not valid:
        # Ask user for number and check it is valid
        try:
            response=int(int(question))
            if response<=0:
                print(error)
            else:
                return response