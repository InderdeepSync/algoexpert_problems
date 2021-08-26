

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


def levenshtein_distance_iterative(string1, string2):  # Verified on Leetcode
    edits = [[x for x in range(len(string2) + 1)] for _ in range(len(string1) + 1)]

    for i in range(1, len(string1) + 1):
        edits[i][0] = edits[i - 1][0] + 1

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1])

    return edits[-1][-1]


if __name__ == "__main__":
    print(levenshtein_distance_iterative("abc", "abc"))