# functions go here

# makes sure answer isnt blank
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response

# checks that number is more than or equal to 2
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response < 2:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine goes here
get_budget = num_check ("What is your budget in dollars? ",
                        "Please enter a number that is 2 or more\n", 
                        int)

print("You said", get_budget)