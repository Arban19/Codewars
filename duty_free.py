# This program works out how many bottles of duty free whiskey you would have to buy such that the savings over the normal high street price would effectively cover the cost of your holiday.

def duty_free(price, discount, holiday_cost):
    """ Inputs are the high street price (price), the duty free discount (discount, in percent) and the total cost of the holiday. """
    savings = price * (discount/100)
    return int(holiday_cost/savings)

print(duty_free(12,50,1000))
