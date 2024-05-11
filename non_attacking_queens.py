
from typing import List


def isValid(position: List):
    # Only need to check whether last number in position is valid.
    n = len(position)
    i = 0
    while i < len(position) and position[i] is not None:
        i += 1

    i -= 1

    for j in range(0, i):
        if position[j] == position[i] or position[i] in (position[j] + (i - j), position[j] - (i - j)):
            return False
    return True


def inner(curPos):
    count = 0

    n = len(curPos)
    i = 0
    while curPos[i] is not None:
        i += 1
        if i == len(curPos):
            count += int(isValid(curPos))
            print(curPos)
            return count

    for j in range(n):
        # j is the possible position of queen in ith row
        posCopy = list(curPos)
        posCopy[i] = j
        if not isValid(posCopy):
            continue

        count += inner(posCopy)

    return count


def nonAttackingQueens(n):  # Verified on AlgoExpert
    start = [None] * n
    return inner(start)


if __name__ == "__main__":
    print(nonAttackingQueens(4))
