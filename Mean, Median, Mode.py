test_list1 = [1,2,2,3,4,5,6,7,8,9,10]
test_list2 = [1,2,3,4,5,6,7,8,9,10]

def mean(nlist):
    total = 0
    for x in nlist:
        total += x
    mean = total/len(nlist)
    return mean




def median(nlist):
    if len(nlist) % 2 == 1:
        a = (len(nlist) - 1) / 2
        median = nlist[int(a)]

    elif len(nlist) % 2 == 0:
        a = nlist[int(len(nlist) / 2)]
        b = nlist[int(len(nlist) / 2 - 1)]
        c = (a + b) / 2
        median = c

    return median

# def mode(nlist):
#     for x in nlist:



