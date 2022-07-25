# Functions go here


def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# checks that number is more than or equal to 5
def price_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def get_grams(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response < 100:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


item = ""

while item != "xxx":

    # ask user for item name
    item = not_blank("Item: ",
                     "This can't be blank")

    # End the loop if the exit code is entered
    if item == "xxx":
        break

    weight_grams = get_grams("What is the weight in grams? ",
                             "Please enter a number that is 100 or more\n", int)

    get_cost = price_check("What is the price in dollars? ",
                           "Please enter a number that is 1 or more\n", float)
