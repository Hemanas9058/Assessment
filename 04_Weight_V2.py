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

def currency(x):
    return "${:.2f}".format(x)


# Main routine goes here
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

pandas.set_option('display.max_columns', None)

add_dollars = ['Cost', 'U.P']
for item in add_dollars:
    price_frame[item] = price_frame[item].apply(currency)

print()
print(price_frame)

unitprice_list.sort()

print("The cheapest item is:", *unitprice_list[:1])