a = [2, 4, 6, 8, 10, 12, 14]
x = 2
def binary_search(a, x, lower=0):

    if lower > len(a) - 1:
        return -1
    else:
        middle = (lower + len(a) - 1) // 2

        if x == a[middle]:
            return middle
        elif x < a[middle]:
            return binary_search(a, x, middle - 1)
        else:
            return binary_search(a, x, middle + 1)

result = binary_search(a, x)

print(result)

#print(a[len(a) // 2]) = 8