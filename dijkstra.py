
from typing import List
from pprint import pprint as pp

import heapq

import math


class Solution:

    def create_graph(self, edges, succProb):
        self.graph = {}
        self.weights = {}
        for i, edge in enumerate(edges):
            s, e = edge

            self.weights[(s, e)] = math.log2(succProb[i]) * -1
            self.weights[(e, s)] = math.log2(succProb[i]) * -1

            if s in self.graph:
                self.graph[s].append(e)
            else:
                self.graph[s] = [e]

            if e in self.graph:
                self.graph[e].append(s)
            else:
                self.graph[e] = [s]

    def dijkstra(self, start_node, end_node):
        state = [float('inf')] * self.n
        state[start_node] = 0

        arr = []
        heapq.heappush(arr, (state[start_node], start_node))
        visited = set()

        while arr:
            _, cur = heapq.heappop(arr)
            if cur in visited:
                continue

            visited.add(cur)
            if cur == end_node:
                break

            for n in self.graph.get(cur, []):
                new_dist = state[cur] + self.weights[(cur, n)]
                state[n] = min(state[n], new_dist)
                heapq.heappush(arr, (state[n], n))

        return state[end_node]

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        self.n = n

        self.create_graph(edges, succProb)
        return math.exp2(-1 * self.dijkstra(start_node, end_node))


if __name__ == '__main__':
    pp(Solution().maxProbability(n = 500, edges = [[193,229],[133,212],[224,465]], succProb = [0.91,0.78,0.64], start_node = 4, end_node = 364))