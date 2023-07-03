a = [2, 4, 6, 8, 10, 12, 14]
x = 12
def binary_search(a, x, lower):
    if lower >= len(a):
        return -1
    else:
        middle = lower + (len(a) - 1) // 2

        if a[middle] == x:
            return middle
        elif a[middle] < x:
            return binary_search(a, x, lower + 1)
        else:
            return binary_search(a, x, lower - 1)
def binary_search_wrapper(a, x):
    return binary_search(a, x, 0)

result = binary_search_wrapper(a, x)

print(result)

#print(a[len(a) // 2]) = 8