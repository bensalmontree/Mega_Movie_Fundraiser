import re
from numpy import var
import pandas

# Function goes here
# WARNING: The response is returned in title case
def string_check(choice,options):
    is_valid=""
    chosen=""
    for var_list in options:
        # If the snack is in one of the lists, return the full name
        if choice in var_list:
            # Get full name of snack and put it in title case so it looks nice when outputted
            chosen=var_list[0].title()
            is_valid="yes"
            break
        else:
            is_valid="no"
            break

# Main routine

pay_method=[
    ["cash","ca"],
    ["credit","cr"]
]

# Loop until exit code...
name=""
while name!="xxx":
    name=input("Name: ")
    if name=="xxx":
        break

    # Ask for payment method
    how_pay="invalid choice"
    while how_pay=="invalid choice":
        how_pay=input("Please choose a payment method (cash or credit)")
        how_pay=string_check(how_pay,pay_method)

    # Ask for subtotal (for testing purposes)
    subtotal=float(input("Sub total? $"))

    if how_pay=="Credit":
        surcharge=0.05*subtotal
    else:
        surcharge=0
    
    total=subtotal+surcharge

    print("Name: {} | Subtotal: ${:.2f} | Surcharge: ${:.2f} | Total Payable: ${:.2f}".format(name,subtotal,surcharge,total))

    # Calculate surcharge