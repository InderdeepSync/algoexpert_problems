import heapq
import math
from typing import List


class Solution:

    def get_distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        # return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return abs(x2 - x1) + abs(y2 - y1)

    def create_edges(self, points):
        edges_heap = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                entry = (self.get_distance(points[i], points[j]), (points[i], points[j]))
                heapq.heappush(edges_heap, entry)

        return edges_heap

    def minCostConnectPoints(self, points: List[List[int]]) -> int: # Verified on Leetcode #1584
        p_sets = []
        hash_map = {}
        merge_count = len(points) - 1

        for i in range(len(points)):
            points[i] = tuple(points[i])

        for p in points:
            temp_set = {p}
            p_sets.append(temp_set)
            hash_map[p] = temp_set

        edges = self.create_edges(points)
        # print(edges)
        min_cost = 0
        while merge_count > 0:
            cost, (src, dest) = heapq.heappop(edges)

            if hash_map[src] is hash_map[dest]:
                continue

            temp = hash_map[src].union(hash_map[dest])
            for n in hash_map[src]:
                hash_map[n] = temp
            for n in hash_map[dest]:
                hash_map[n] = temp
            merge_count -= 1
            min_cost += cost
            print(cost)

        return min_cost


if __name__ == '__main__':
    # This is the Kruskal's Algorithm
    print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
