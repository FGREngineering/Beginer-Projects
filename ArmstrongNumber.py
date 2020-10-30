# Armstrong Number

def anumber(number):
    ptext = "{} is an Armstrong number".format(number)
    ntext = "{} is not an Armstrong number".format(number)
    if len(str(number)) == 1:
        return ptext
    else:
        total = 0
        for x in str(number):
            total += int(x) ** len(str(number))
        if total == number:
            return ptext, total, number
        else:
            return ntext, total, number


print(anumber(1634))
print(anumber(10))
print(anumber(768549))
