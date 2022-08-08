# Functions go here
import pandas


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

def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = string_check("Would you like to read the instructions?", options)

    if show_help == "yes":
        print()
        print("**** Price Comparison ****")
        print()
        print("This program will help you to compare prices"
              "\nof products and show you the best value item."
              "\nIn order to use this program you will be asked"
              "\nto input your budget, the name of your item,"
              "\nthe weight, and the cost of the item. After you"
              "\nhave inputted all of your data the exit code"
              "\n'xxx' may be input to continue the code and have."
              "\na list printed. This list will be sorted in ascending"
              "\norder and the item at the top of the list will be best"
              "\nvalue per kg/L.")
        print()

    return ""

def currency(x):
    return "${:.2f}".format(x)


# Main routine goes here

# valid options for yes / no questions
yes_no_list = [
    ["yes", "y"],
    ["no", "n"]
]

# Ask if instructions are needed
instructions(yes_no_list)
print()

budget = get_budget("What is your budget in dollars? ",
                    "Please enter a number that is 5 or more\n", float)
print("Your budget is", "${:.2f}".format(budget))

# set up lists
item_list = []
weight_list = []
cost_list = []
unitprice_list = []

variable_dict = {
        'Item': item_list,
        'Weight (g)': weight_list,
        'Cost': cost_list,
        'Unit Price': unitprice_list,
    }


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

    # add item name, weight, price, and unit price to lists
    item_list.append(item)
    weight_list.append(weight_grams)
    cost_list.append(get_cost)
    unitprice_list.append(unit_price)

price_frame = pandas.DataFrame(variable_dict)
price_frame = price_frame.set_index('Item')

price_frame = price_frame.rename(columns={'Unit Price': 'U.P',
                                          'Weight (g)': 'grams'})

price_frame = price_frame.sort_values(by=['U.P'])

pandas.set_option('display.max_columns', None)

add_dollars = ['Cost', 'U.P']
for item in add_dollars:
    price_frame[item] = price_frame[item].apply(currency)

print()
print("Budget:", "${:.2f}".format(budget))
print()
print(price_frame)
print()
print("The items are listed in ascending order by unit price.",
      "\nThe ones at the top are the best value.")
