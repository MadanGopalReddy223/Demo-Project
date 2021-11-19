l=[15,5,20,1,7]
def listMinMax(l):
    print("I am adding code from my local")
    print("I am adding a line from other developer")
    min =l[0]
    max =l[1]
    for x in l:
        if x < min:
            min = x
        elif x > max:
            max = x
    return min, max

def listSort(l):
    sort = sorted(l)
    return sort

def listReverse(l):
    return l[::-1]

def listlength(l):
    return len(l)




