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


def index_equals_value(sorted_input, start, end):
    min_index = float("inf")
    while start <= end:
        mid = (start + end) // 2
        if sorted_input[mid] > mid:
            end = mid - 1
        elif sorted_input[mid] == mid:
            min_index = min(min_index, mid)
            end = mid - 1
        else:
            start = mid + 1

    return min_index


def search_for_range(arr, target, start, end):  # Verified on Leetcode
    if start > end:
        return [-1, -1]

    mid = math.floor((start + end) / 2)
    if arr[mid] == target:
        temp = mid - 1
        while temp >= 0 and arr[temp] == target:
            temp -= 1

        temp2 = mid + 1
        while temp2 <= len(arr) - 1 and arr[temp2] == target:
            temp2 += 1

        return [temp + 1, temp2 - 1]
    elif arr[mid] > target:
        return search_for_range(arr, target, start, mid - 1)
    else:
        return search_for_range(arr, target, mid + 1, end)


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
    print("Index Equals Value: {}".format(index_equals_value([-5, -3, 2, 3, 4, 5, 9], start=0, end=6)))
    print("Search For Range: {}".format(search_for_range([5, 7, 7, 8, 8, 10], 8, start=0, end=5)))
