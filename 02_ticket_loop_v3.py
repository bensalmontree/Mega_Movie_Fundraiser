# Start of loop

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
    name=input("Name: ")
    count+=1

if count==MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. There are {} places still available".format(count, MAX_TICKETS - count))