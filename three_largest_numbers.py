

def k_largest_numbers(arr, k):
    res = []

    for item in arr:
        res.append(item)

        res.sort(reverse=True)
        res = res[:k]

    return res


if __name__ == "__main__":
    result = k_largest_numbers([9, 6, 15, 4, 22, 1, 35, -2, 11], 3)
    print(result)