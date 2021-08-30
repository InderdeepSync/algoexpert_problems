
def move_element_to_end(arr, target):  # Verified on Leetcode (My Solution)
    last_index = 0

    for i in range(len(arr)):
        if arr[i] != target:
            arr[i], arr[last_index] = arr[last_index], arr[i]
            last_index += 1

    return arr


def move_element_to_end2(arr, target):  # Alternate Solution via Double Pointers
    j = len(arr) - 1
    i = 0

    while i < j:
        while arr[j] == target:
            j = j - 1

        if arr[i] == target:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1

        i += 1

    return arr


if __name__ == "__main__":
    result = move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2)
    print(result)