
def _count_inversions(arr, start, end):  # Verified on HackerRank
    if start >= end:
        return 0

    mid = (start + end) // 2

    left_count = _count_inversions(arr, start, mid)
    right_count = _count_inversions(arr, mid + 1, end)

    sorted_arr = []
    no_of_inversions = 0

    left_ptr = start
    right_ptr = mid + 1
    while left_ptr <= mid and right_ptr <= end:
        if arr[left_ptr] <= arr[right_ptr]:
            sorted_arr.append(arr[left_ptr])
            left_ptr += 1
        else:
            no_of_inversions += mid - left_ptr + 1
            sorted_arr.append(arr[right_ptr])
            right_ptr += 1

    sorted_arr += arr[left_ptr:mid + 1] + arr[right_ptr: end + 1]

    for i in range(len(sorted_arr)):
        arr[start + i] = sorted_arr[i]
    return left_count + right_count + no_of_inversions


if __name__ == "__main__":
    input_arr = [7, 5, 3, 1]
    print("Count Inversions: {}".format(_count_inversions(input_arr, 0, len(input_arr) - 1)))