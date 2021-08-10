

def bubble_sort(arr):
    print("Original Array: {}".format(arr))
    for index_i in range(len(arr)):
        for index_j in range(index_i + 1, len(arr)):
            if arr[index_i] > arr[index_j]:
                temp = arr[index_i]
                arr[index_i] = arr[index_j]
                arr[index_j] = temp

            print("After One Inner Iteration: {}".format(arr))

        print("After One Outer Iteration: {}".format(arr))

    return arr


def selection_sort(arr):
    for index_i in range(len(arr)):
        minimum = arr[index_i]
        min_index = index_i

        for index_j in range(index_i + 1, len(arr)):
            if arr[index_j] < minimum:
                minimum = arr[index_j]
                min_index = index_j

        temp = arr[index_i]
        arr[index_i] = minimum
        arr[min_index] = temp

    return arr


def insertion_sort(arr):
    sorted_arr_boundary = -1
    for index_i in range(len(arr)):
        sorted_arr_boundary += 1
        for index_j in range(sorted_arr_boundary, 0, -1):
            if arr[index_j] < arr[index_j - 1]:
                temp = arr[index_j]
                arr[index_j] = arr[index_j - 1]
                arr[index_j - 1] = temp
            else:
                break
    return arr


if __name__ == "__main__":
    array = [4, 9, 1, 7, -3, 10, 0, -8, 9]

    sorted_arr = insertion_sort(array)

    print(sorted_arr)
