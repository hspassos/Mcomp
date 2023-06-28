x = 25
y = 10

def min(x, y):
    if x >= y:
        return y
    else:
        return x

def max_divisor(x, y):
    div = min(x, y)

    while x % div != 0 or y % div != 0:
        div = div - 1
    print (div)

