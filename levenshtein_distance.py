

def levenshtein_distance(string1, string2):
    if len(string1) == 0:
        return len(string2)
    elif len(string2) == 0:
        return len(string1)

    temp1 = levenshtein_distance(string1[1:], string2[1:])
    if string1[0] == string2[0]:
        return temp1
    else:
        return 1 + min(temp1, levenshtein_distance(string1[1:], string2), levenshtein_distance(string1, string2[1:]))


if __name__ == "__main__":
    print(levenshtein_distance("abc", "yabd"))