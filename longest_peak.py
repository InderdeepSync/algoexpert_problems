def longest_peak(arr):  # Accepted on LeetCode
    max_length = 0
    for i in range(1, len(arr) - 1):
        if not arr[i - 1] < arr[i] > arr[i + 1]:
            continue

        j = i + 2
        while j < len(arr) and arr[j] < arr[j - 1]:
            j += 1

        k = i - 2
        while k >= 0 and arr[k] < arr[k + 1]:
            k -= 1

        max_length = max(max_length, (j - 1) - (k + 1) + 1)  # final - initial + 1

    return max_length


if __name__ == "__main__":
    print(longest_peak([2, 1, 4, 7, 3, 2, 5]))
