
from pprint import pprint as pp
from typing import List
import heapq

def traverse(start, graph):
    # returns traversed nodes
    queue = [start]
    visited = set()

    while queue:
        cur = queue.pop(0)
        visited.add(cur)

        for neighbor in filter(lambda n: n not in visited, graph[cur]):
            queue.append(neighbor)

    return visited


def dfs(cur, graph, visited, calculating: List, scores, ring):
    if cur in visited:
        return scores[cur]
    if cur in calculating:
        raise Exception()

    calculating.append(cur)
    reachable = set()
    for neighbor in graph[cur]:
        reachable.add(neighbor)
        try:
            reachableFromNeighbor = dfs(neighbor, graph, visited, calculating, scores, ring)
            # reachable.add(neighbor)
            reachable.update(reachableFromNeighbor)
        except:
            ring.append(calculating[calculating.index(neighbor):])

    # reachable.update(set(graph))
    calculating.pop()
    visited.add(cur)
    scores[cur] = reachable
    return reachable
    # returns list of airports reachable, not including itself


def assignScores(graph, start, reachable):
    visited = set()
    scores = {}
    for airport in graph.keys():
        scores[airport] = set()

    ring = []
    while len(visited) < len(graph):
        notVisited = set(graph.keys()).difference(visited)
        cur = list(notVisited)[0]
        dfs(cur, graph, visited, [], scores, ring)

    for r in ring:
        merged = set()
        for a in r:
            merged = merged.union(scores[a])
        for a in r:
            mergedCopy = set(merged) - {a}
            scores[a] = mergedCopy
    for cur, scoreSet in scores.items():
        scoreSet.difference_update(reachable)
        scoreSet.discard(cur)
        scoreSet.discard(start)


    pp(scores)
    # print(ring)
    return scores


def airportConnections(airports, routes, startingAirport): # Verified on Algoxpert
    routesMap = {}
    for airport in airports:
        routesMap[airport] = set()
    for route in routes:
        src, dest = route
        # print(src, dest)
        routesMap[src].add(dest)

    reachable = traverse(startingAirport, routesMap)
    # print(reachable)
    unreachable = set(routesMap.keys()).difference() - reachable
    scores = assignScores(routesMap, startingAirport, reachable)

    heap = []
    for ap, reachable in scores.items():
        heapq.heappush(heap, (-1 * len(reachable), ap))

    connections = 0
    while unreachable:
        if not heap:
            connections += len(unreachable)
            break
        _, airport = heapq.heappop(heap)
        if len(unreachable.intersection(scores[airport])) > 0:
            connections += 1
            unreachable.difference_update(scores[airport])
            unreachable.difference_update({airport})
    return connections


if __name__ == "__main__":
    airports_list = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]
    routes = [
        ["LGA", "DSM"],
        ["DSM", "ORD"],
        ["SIN", "BGI"],
        ["SIN", "CDG"],
        ["CDG", "DEL"],
        ["DEL", "DOH"],
        ["DEL", "CDG"],
        ["DEL", "EWR"],
        ["HND", "ICN"],
        ["ICN", "JFK"],
        ["JFK", "LGA"],
        ["JFK", "SFO"],
        ["EYW", "LHR"],
        ["SFO", "ORD"],
        ["SFO", "LGA"]
    ]
    print("Airport Connections: {}".format(airportConnections(airports_list, routes, "LGA")))
