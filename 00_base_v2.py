# functions go here


# checks that questions are not left blank and repeat question
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# checks that the budget is 5 or more
def get_budget(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response < 5:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks that number is more than or equal to 1
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


# checks that grams is at least 100
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


# Main routine goes here
budget = get_budget("What is your budget in dollars? ",
                    "Please enter a number that is 5 or more\n", float)
print("Your budget is", "${:.2f}".format(budget))

item = ""

while item != "xxx":

    # ask user for item name
    item = not_blank("Item: ",
                     "This can't be blank")

    # End the loop if the exit code is entered
    if item == "xxx":
        break

    # get weight in grams
    weight_grams = get_grams("What is the weight in grams / milliliters? ",
                             "Please enter a number that is 100 or more\n", int)

    # get cost in dollars
    get_cost = price_check("What is the price in dollars? ",
                           "Please enter a number that is 1 or more\n", float)

    # test unit price calculation
    unit_price = get_cost / (weight_grams / 1000)
    print("The unit price is", "${:.2f}".format(unit_price))
