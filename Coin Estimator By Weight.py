import math

wpennies = input("What is the weight of your pennies?:")
wnickels = input("What is the weight of your nickels?:")
wdimes = input("What is the weight of your dimes?:")
wquarters = input("What is the weight of your quarters?:")

npennies = int(wpennies) / 2.5
nnickels = int(wnickels) / 5
ndimes = int(wdimes) / 2.268
nquarters = int(wquarters) / 5.670

pwrappers = math.ceil(npennies / 50)
nwrappers = math.ceil(nnickels / 40)
dwrappers = math.ceil(ndimes / 50)
qwrappers = math.ceil(nquarters / 40)


txt = "You will need {} wrappers for your {} pennies, {} wrappers for your {} nickels, {} wrappers for your {} dimes, and {} wrappers for your {} quarters."

print(txt.format(pwrappers, npennies, nwrappers, nnickels, dwrappers, ndimes, qwrappers, nquarters))

