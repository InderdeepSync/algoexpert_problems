def three_number_sum(arr, target):
    arr.sort()
    res = []

    for index in range(len(arr)):
        start = index + 1
        end = len(arr) - 1

        while start < end:
            projected_sum = arr[index] + arr[start] + arr[end]
            if projected_sum == target:
                res.append((arr[index], arr[start], arr[end]))
                start += 1
                end -= 1
            elif projected_sum > target:
                end -= 1
            else:
                start += 1

    return res


if __name__ == "__main__":
    result = three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    print(result)
