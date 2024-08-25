from typing import List
from pprint import pprint as pp


def dfs(cur, edges, visited, calculating, ring):
    if cur in visited:
        return
    if cur in calculating:
        raise Exception()

    calculating.append(cur)
    for neighbor in edges[cur]:
        try:
            dfs(neighbor, edges, visited, calculating, ring)
            # reachable.add(neighbor)
        except:
            ring.append(calculating[calculating.index(neighbor):])

    calculating.pop()
    visited.add(cur)


def no_disjoint_sets(set_list):
    for i in range(len(set_list) - 1):
        flag = True
        for j in range(i + 1, len(set_list)):
            if not set_list[i].isdisjoint(set_list[j]):
                flag = False
        if flag:
            return False

    return True


def twoEdgeConnectedGraph(edges):
    visited = set()
    ring = []

    if len(edges) <= 1:
        return True
    # notVisited = set(range(len(graph))).difference(visited)
    cur = 0
    dfs(cur, edges, visited, [], ring)

    nodes = set()
    rings = list(filter(lambda r: len(r) > 2, ring))
    print(rings)

    for nodeSet in rings:
        # print(nodeSet)
        for node in nodeSet:
            nodes.add(node)

    return len(nodes) == len(edges) and no_disjoint_sets([set(r) for r in rings])


if __name__ == "__main__":
    graph = [
        [1, 2, 5],
        [0, 2],
        [0, 1, 3],
        [2, 4, 5],
        [3, 5],
        [0, 3, 4]
      ]
    print(twoEdgeConnectedGraph(graph))