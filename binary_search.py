import math


def binary_search(arr, value, start, end):
    if start > end:
        return None

    mid = math.floor((start + end) / 2)
    if arr[mid] == value:
        return mid
    elif arr[mid] > value:
        return binary_search(arr, value, start, mid - 1)
    else:
        return binary_search(arr, value, mid + 1, end)


if __name__ == '__main__':
    array = [12, 45, 65, 78, 83, 87, 91, 95, 99, 101]
    result = binary_search(array, 86, 0, len(array) - 1)
    print(result)
