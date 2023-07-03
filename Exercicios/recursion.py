a = [2, 4, 6, 8, 10, 12, 14]
x = 2
def binary_search(a, x, l):

    middle = len(a) - 1 - l

    if x == a[middle]:
        return middle
    else:
        return binary_search(a, x, l + 1)
"""    elif x > a[middle]:
        return mid + 1 + binary_search(a[middle + 1:], x)
"""
def binary_search_wrapper(a, x):
    return binary_search(a, x, 0)

result = binary_search_wrapper(a, x)

print(result)

#print(a[len(a) // 2]) = 8