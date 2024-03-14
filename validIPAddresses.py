def isValid(string):
    if not string:
        return False

    if int(string) == 0 and len(string) > 1:
        return False

    if len(string) > 1 and string[0] == "0":
        return False

    if int(string) > 255:
        return False
    return True


def inner(string, dotCount):
    if dotCount == 0:
        return [string] if isValid(string) else []

    result = []
    for i in range(1, 4):
        temp = string[:i]
        if not isValid(temp):
            break

        remaining = inner(string[i:], dotCount - 1)
        for rem in remaining:
            result.append(temp + "." + rem)

    return result


def validIPAddresses(string):
    return inner(string, 3)
