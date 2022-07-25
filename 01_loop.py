# functions go here

def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# Main routine goes here

item = ""

while item != "xxx":

    # ask user for item name
    item = not_blank("Item: ",
                     "This can't be blank")

    # End the loop if the exit code is entered
    if item == "xxx":
        break