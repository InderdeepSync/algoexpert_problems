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


def search_in_sorted_matrix(input_matrix, target, start, end):
    if start[0] > end[0] or start[1] > end[1]:
        return None

    mid = (math.floor((start[0] + end[0]) / 2), math.floor((start[1] + end[1]) / 2))

    current = input_matrix[mid[0]][mid[1]]
    if current == target:
        return mid
    elif current > target:
        return search_in_sorted_matrix(input_matrix, target, start, (mid[0], mid[1]))
    else:
        return search_in_sorted_matrix(input_matrix, target, (mid[0], mid[1]), end)


def shifted_binary_search(arr, start, end, target):  # Verified on LeetCode
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] >= arr[start]:
            if arr[mid] > target >= arr[start]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] < target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


if __name__ == '__main__':
    array = [12, 45, 65, 78, 83, 87, 91, 95, 99, 101]
    result = binary_search(array, 86, 0, len(array) - 1)

    matrix = [[1, 4, 7, 12, 15, 1000],
              [2, 5, 19, 31, 32, 1001],
              [3, 8, 24, 33, 35, 1002],
              [40, 41, 42, 44, 45, 1003],
              [99, 100, 103, 106, 108, 1004]]
    found_coordinates = search_in_sorted_matrix(matrix, 44, start=(0, 0), end=(len(matrix) - 1, len(matrix[0]) - 1))
    print(found_coordinates)

    print("Shifted Binary Search: {}".format(shifted_binary_search([3, 1], start=0, end=1, target=1)))
