a = [2, 4, 6, 8, 10, 12, 14]
x = 12
def binary_search(a, x, lower=0):
    if lower >= len(a):
        return -1

    mid = (lower + len(a)) // 2

    if a[mid] == x:
        return mid
    elif a[mid] < x:
        return binary_search(a, x, mid + 1)
    else:
        return binary_search(a, x, lower, mid - 1)

result = binary_search(a, x)

print(result)