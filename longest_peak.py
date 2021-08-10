

def longest_peak(arr):
    lengths = []
    for i in range(1, len(arr) - 1):
        if not arr[i-1] < arr[i] > arr[i+1]:
            continue

        j = i + 2
        while arr[j] < arr[j - 1] and j < len(arr):
            j += 1

        k = i - 2
        while arr[k] < arr[k+1] and k >= 0:
            k -= 1

        lengths.append((j - 1) - (k + 1) + 1)  # final - initial + 1

    return max(lengths)








if __name__ == "__main__":
    print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))