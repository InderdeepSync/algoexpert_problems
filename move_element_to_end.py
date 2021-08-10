
def move_element_to_end(arr, target):
    last_index = 0

    for i in range(len(arr)):
        if arr[i] != target:
            temp = arr[i]
            arr[i] = arr[last_index]
            arr[last_index] = temp

            last_index += 1

    return arr


if __name__ == "__main__":
    result = move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2)
    print(result)