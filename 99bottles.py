#99 Bottles


x = 99
counter = 99
next = counter - 1

while x > 0:

    line = "{c} bottles of beer on the wall, {c} bottles of beer.Take one down, pass it around, {n} bottles of beer on the wall...".format(c = counter, n = next)

    print(line)
    
    x -= 1
    counter -= 1
    next -= 1
