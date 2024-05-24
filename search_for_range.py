
def inner(array, start, end, target):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        result = [mid, mid]
        temp1 = inner(array, mid + 1, end, target)
        temp2 = inner(array, start, mid - 1, target)

        if temp1:
            result[1] = temp1[1]
        if temp2:
            result[0] = temp2[0]
        return result
    elif array[mid] < target:
        return inner(array, mid + 1, end, target)
    else:
        return inner(array, start, mid - 1, target)


def searchForRange(array, target): # Verified on AlgoExpert
    # Write your code here.
    result = inner(array, 0, len(array) - 1, target)
    return result if result else [-1, -1]


if __name__ == "__main__":
    print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
