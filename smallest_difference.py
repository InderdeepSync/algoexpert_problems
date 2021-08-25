import math

def smallest_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()

    smallest_diff = math.inf
    res = None

    arr1_index = arr2_index = 0

    while arr1_index < len(arr1) and arr2_index < len(arr2):
        current_diff = arr1[arr1_index] - arr2[arr2_index]

        if abs(current_diff) < smallest_diff:
            smallest_diff = abs(current_diff)
            res = [arr1[arr1_index], arr2[arr2_index]]

        if current_diff < 0:
            arr1_index += 1
        else:
            arr2_index += 1

    return res


if __name__ == "__main__":
    result = smallest_difference([-1, 5, 10, 21, 28, 3], [26, 134, 135, 15, 17])
    print(result)