import math


def patternMatcher(pattern, string): # Verified on AlgoExpert
    # Write your code here.
    isSwapped = False
    if pattern[0] == "y":
        pattern = pattern.replace("x", "t").replace("y", "x").replace("t", "y")
        isSwapped = True

    if pattern.count("x") == len(string):
        if len(string) % 4 != 0:
            return False
        x = string[0: len(string) // 4]
        if string == "".join(map(lambda c: x, pattern)):
            return [x, ""] if not isSwapped else ["", x]

    xCount = pattern.count("x")
    yCount = pattern.count("y")
    xBeg = len(pattern) - len(pattern.lstrip('x'))
    # yBeg = len(pattern.lstrip('x')) - len(pattern.lstrip('x').lstrip('y'))

    for i in range(1, math.ceil(len(string) / xCount)):
        x = string[:i]
        yTotal = (len(string) - xCount * len(x))
        if yTotal % yCount != 0:
            continue

        yLen = yTotal // yCount
        y = string[xBeg * len(x): xBeg * len(x) + yLen]
        joined = map(lambda c: x if c == "x" else y, pattern)

        if "".join(joined) == string:
            return [x, y] if not isSwapped else [y, x]

    return []


if __name__ == "__main__":
    print(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"))