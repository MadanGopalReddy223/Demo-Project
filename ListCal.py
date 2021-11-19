l=[15,5,20,1,7]
def listMinMax(l):
    min =l[0]
    max =l[1]
    for x in l:
        if x < min:
            min = x
        elif x > max:
            max = x
    return min, max

