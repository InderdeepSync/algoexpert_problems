import math


def getNeighbors(x, y, visited):
    steps = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
    result = []
    for step in steps:
        result.append((x + step[0], y + step[1]))

    return filter(lambda c: c not in visited, result)


def inner(start, end, visited):
    queue = [(start, 0)]
    while queue:
        cur, dist = queue.pop(0)
        if cur == end:
            return dist

        for neighbor in getNeighbors(cur[0], cur[1], visited):
            queue.append((neighbor, dist + 1))
            visited.add(neighbor) # TODO: Why here?? and not immediately after queue.pop(0) on line 16


def knight_connection(knightA, knightB): # Verified on AlgoExpert
    return math.ceil(inner(tuple(knightA), tuple(knightB), visited=set()) / 2)


if __name__ == "__main__":
    print(knight_connection([10, 10], [-10, -10]))
