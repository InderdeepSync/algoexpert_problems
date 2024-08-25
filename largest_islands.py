def findIslands(matrix):
    visited = set()

    def getValidNeighbors(x, y):
        res = []
        for c in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if 0 <= c[0] < len(matrix) and 0 <= c[1] < len(matrix[0]) and c not in visited and matrix[c[0]][c[1]] == 0:
                res.append(c)
        return res

    islands = {}
    nodeToIslandMap = {}
    islandIdx = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 or (i, j) in visited:
                continue
            visited.add((i, j))
            islands[islandIdx] = {(i, j)}
            nodeToIslandMap[(i, j)] = islandIdx
            extended = getValidNeighbors(i, j)
            while extended:
                node = extended.pop()
                visited.add(node)
                nodeToIslandMap[node] = islandIdx
                islands[islandIdx].add(node)
                extended.extend(getValidNeighbors(node[0], node[1]))

            islandIdx += 1

    return islands, nodeToIslandMap


def largestIsland(matrix):
    def getOneAway(x, y):
        res = []
        for c in [(x - 1, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x + 1, y - 1), (x + 2, y), (x - 2, y), (x, y - 2),
                  (x, y + 2)]:
            if 0 <= c[0] < len(matrix) and 0 <= c[1] < len(matrix[0]) and matrix[c[0]][c[1]] == 0:
                res.append(c)
        return res

    islands, nodeToIslandMap = findIslands(matrix)
    largestIsland = min(len(matrix[0]) * len(matrix), len(max(islands.values() or [[]], key=len)) + 1)
    for islandIdx, nodes in islands.items():
        for node in nodes:
            for oneAway in getOneAway(node[0], node[1]):
                largestIsland = max(largestIsland, len(nodes) + len(islands[nodeToIslandMap[oneAway]]))

    return largestIsland



if __name__ == "__main__":
    print(largestIsland([
        [1]
    ]))
