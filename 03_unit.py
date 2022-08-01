# Functions go here


def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# checks specifically for yes / no - change error message if generalising
def string_check(question, options):

    is_valid = ""

    valid = False
    while not valid:

        choice = input(question)

        for var_list in options:

            # if the snack is in one of the lists, return the full name
            if choice in var_list:

                # Get full name of snack and put it
                # in title case so it looks nice when outputted
                chosen = var_list[0]
                is_valid = "yes"
                break

            # if the chosen option is not valid, set is_valid to no
            else:
                is_valid = "no"

                # if choice is not OK, repeat question
        if is_valid == "yes":
            return chosen

        else:
            print("Please enter yes / no")
            print()
            # return "invalid choice"


def get_unit(question):

    # Initialise variables and error message
    error = "Please enter a unit"

    valid = False
    while not valid:

        # ask for profit goal..
        response = not_blank("What is the unit for your weight (eg g, kg, ml, l) ",
                             "Please enter a unit")

        # check if last character is g
        if response[-1] == "g":
            unit = "grams"
            # Get amount (everything before the g)
            weight = response[:-1]

        # check if last character is ml
        if response[-1] == "kg":
            unit = "kilograms"
            # Get amount (everything before the kg)
            weight = response[:-1]

        # check if last character is ml
        if response[-1] == "ml":
            unit = "milliliters"
            # Get amount (everything before the ml)
            weight = response[:-1]

        # check if last character is l
        if response[-1] == "l":
            unit = "liters"
            # Get amount (everything before the ml)
            weight = response[:-1]

        else:
            # set response to amount for now
            unit = "unknown"
            weight = response

        try:
            # Check amount is a number more than zero...
            unit = float(weight)
            if unit <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if unit == "unknown" and weight >= 100:
            unit_type = string_check("Do you mean {}g ie {} grams? , y / n".format(weight, weight),
                                     yes_no_list)

            # Set profit type based on user answer above
            if unit_type == "yes":
                unit = "grams"
            else:
                unit = "milliliters"

        elif unit == "unknown" and weight < 100:
            big_unit_type = string_check("Do you mean {}L ie {} Liters? , y / n".format(weight, weight)
                                         , yes_no_list)
            if big_unit_type == "yes":
                unit = "liters"
            else:
                unit = "kilograms"

        # return profit goal to main routine
        return weight

# valid options for yes / no questions
yes_no_list = [
    ["yes", "y"],
    ["no", "n"]
]

unit = get_unit("please enter the weight and unit e.g 100g?")

