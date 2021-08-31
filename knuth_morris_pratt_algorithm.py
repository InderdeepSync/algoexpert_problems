

def knuth_morris_pratt_algorithm(string, substring):
    pattern = build_pattern(substring)

    i = j = 0
    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return False


def build_pattern(substring):
    pattern = [-1 for _ in substring]
    i = 1
    j = 0
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern


if __name__ == "__main__":
    print("Is substring contained in string: {}".format(knuth_morris_pratt_algorithm("ababa", "ba")))