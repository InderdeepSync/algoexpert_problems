
def bestDigits(number, numDigits): # Verified on AlgoExpert
    digits = list(map(int, list(number)))

    for i in range(numDigits):
        j = 0
        while (j + 1) < len(digits) and digits[j + 1] < digits[j]:
            j += 1

        del digits[j]

    return "".join(map(str, digits))


if __name__ == "__main__":
    print(bestDigits("462839", 2))