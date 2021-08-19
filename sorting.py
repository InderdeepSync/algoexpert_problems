
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

def quick_sort(arr):
    result_arr = arr.copy()
    _quick_sort(result_arr, 0, len(arr) - 1)
    return result_arr

def _quick_sort(arr, start, last):
    if start >= last:
        return

    pivot_index = start
    pivot = arr[pivot_index]

    beg = pivot_index + 1
    end = last
    while end >= beg:
        if arr[beg] >= pivot >= arr[end]:
            arr[beg], arr[end] = arr[end], arr[beg]
        if arr[end] >= pivot:
            end -= 1
        if arr[beg] <= pivot:
            beg += 1

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    _quick_sort(arr, start, end - 1)
    _quick_sort(arr, end + 1, last)


def quick_select(arr, k):  # Kth Largest Element (Verified on leetCode)
    if not (len(arr) >= k >= 1):
        raise Exception("Invalid Input", k)
    return _quick_select(arr, 0, len(arr) - 1, len(arr) - k)

# noinspection DuplicatedCode
def _quick_select(arr, start, last, k):
    if start == last:
        return arr[start]

    pivot = arr[start]
    beg = start + 1
    end = last
    while end >= beg:
        if arr[beg] >= pivot >= arr[end]:
            arr[beg], arr[end] = arr[end], arr[beg]
        if arr[end] >= pivot:
            end -= 1
        if arr[beg] <= pivot:
            beg += 1

    arr[start], arr[end] = arr[end], arr[start]
    if end == k:
        return arr[end]
    elif end > k:
        updated_start = start
        updated_end = end - 1
    else:
        updated_start = end + 1
        updated_end = last

    return _quick_select(arr, updated_start, updated_end, k)



if __name__ == "__main__":
    array = [4, 9, 1, 7, -3, 10, 0, -8, 9]

    sorted_arr = quick_sort(array)
    print(sorted_arr)

    print("Quick Select: {}".format(quick_select(array, 4)))

