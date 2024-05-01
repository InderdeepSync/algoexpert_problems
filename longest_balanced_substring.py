from typing import List


def longestBalancedSubstring(string): # My Solution Verified on AlgoExpert
    stack: List = []
    lbsLength = 0
    prevCarry = 0
    for index, char in enumerate(string):
        if char == "(":
            stack.append((index, prevCarry))
            prevCarry = 0
        else:
            prevCarry = 0
            if len(stack) == 0:
                continue

            idx, carry = stack.pop()
            strLen = index - idx + 1 + carry
            lbsLength = max(lbsLength, strLen)
            prevCarry = strLen

    return lbsLength


if __name__ == "__main__":
    print("Longest Balanced Substring: {}".format(longestBalancedSubstring("(()))(")))