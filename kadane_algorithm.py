
def kadane_algorithm_alternative(arr):
    """
    Verified on LeetCode
    :param arr:
    :return:
    """
    if not list(filter(lambda num: num >= 0, arr)):
        return max(arr)

    max_sum = running_sum = neg_sum = 0

    for item in filter(lambda num: num != 0, arr):
        if item > 0:
            running_sum += max(neg_sum + item, 0)
            neg_sum = min(neg_sum + item, 0)
            max_sum = max(max_sum, running_sum)
        else:
            neg_sum = neg_sum + item
            if running_sum + neg_sum <= 0:
                running_sum = neg_sum = 0

    return max_sum


def kadane_algorithm_original(arr):
    pass # TODO: Implement it









if __name__ == "__main__":
    print(kadane_algorithm_alternative([3, 500, -1, -9000, 1, 3, -2, 3, 4, 0, 7, 2, -9, 6, 3, 1, -5, -400, 1]))