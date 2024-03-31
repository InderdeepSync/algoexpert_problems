

def inner(arr, select):
    if select == 0:
        return 0
    if select > len(arr):
        return float("-inf")

    if select == len(arr):
        return sum((1 if i % 2 == 0 else -1) * num for i, num in enumerate(arr))

    fn = max if select % 2 == 0 else min
    return fn(inner(arr[1:], select=select), arr[0] - inner(arr[1:], select=select - 1))


def maximizeExpression(array): # Verified on AlgoExpert
    res = inner(array, select=4)
    return 0 if res == float("-inf") else res


if __name__ == "__main__":
    print(maximizeExpression([1, -1, 1, -1, -2]))
    # print(inner([-1, 1, -1, -2], select=3))
    print(inner([1, -1, -2], select=2))