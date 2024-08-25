
def inner(str, numbers):
    if len(str) == 0 or str in numbers:
        return 0

    min_spaces = float("inf")
    for i in range(1, len(str)):
        temp = str[:i]
        if temp in numbers:
            min_spaces = min(min_spaces, 1 + inner(str[i:], numbers))

    return min_spaces

def numbersInPi(pi, numbers):
    return inner(pi, numbers)


if __name__ == "__main__":
    print("Numbers In Pi: ", numbersInPi("3141592653589793238462643383279", ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]))