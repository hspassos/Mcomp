arr = [2, 4, 6, 8, 10, 12, 14]
target = 12
def binary_search(arr, target, left=0):
    if left >= len(arr):
        return -1

    mid = (left + len(arr)) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1)
    else:
        return binary_search(arr, target, left, mid - 1)

result = binary_search(arr, target)

print(result)