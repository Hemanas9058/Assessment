# import libraries

# functions go here


# makes sure answers to questions arent blank
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# checks yes no questions
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

            response = input(question).lower()

            for var_item in to_check:
                if response == var_item:
                    return response
                elif response == var_item[0]:
                    return var_item

            print("Please enter either yes or no...\n")


# checks that number is more than or equal to 5
def num_check(question, error, num_type):
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


# Main routine goes here
get_budget = num_check("What is your budget in dollars? "
                       "Please enter a number that is 5 or more\n", int)

print("You said", get_budget)

item = ""

while item != "xxx":

    # ask user for item name
    item = not_blank("Item: "
                     "This can't be blank")

    # End the loop if the exit code is entered
    if item == "xxx":
        break

    get_cost = num_check ("What is the price in dollars? "
                          "Please enter a number that is 5 or more\n", int)