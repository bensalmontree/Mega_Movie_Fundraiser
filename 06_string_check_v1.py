# String checking functiions, takes in question and list of valid responses
import string


def string_checker(question,to_check):
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
            
# Main routine
for items in range(0,6):
    want_snack=string_checker("Do you want snacks? ",["yes","no"])
    print("Answer OK, you said:",want_snack)
    print()