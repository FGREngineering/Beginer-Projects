import math
from decimal import Decimal

print("Welcome to Change Calculator")
play = input("Start? (Y/N):")

while play == "Y":
    mgiven = input("How much money was handed to you?:")
    itemp = input("What was the price of the item:?")
    change = Decimal(mgiven) - Decimal(itemp)
    schange = str(change)
    schange2 = schange.replace(".", "")
    schange3 = int(schange2)
    nquarters = math.floor(schange3 / 25)
    schange4 = schange3 - (25 * nquarters)
    ndimes = math.floor(schange4 / 10)
    schange5 = schange4 - (10 * ndimes)
    nnickels = math.floor(schange5 / 5)
    schange6 = schange5 - (5 * nnickels)
    npennies = int(schange6 / 1)

    txt = "The change due is {}. Please give the customer {} pennies, {} nickels, {} dimes, and {} quarters"
    input
    print(txt.format(change, npennies, nnickels, ndimes, nquarters))
    play = input("Continue? (Y/N):")

