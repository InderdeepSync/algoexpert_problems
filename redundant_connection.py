from typing import List


class Solution:
    def inner(self, cur):
        if cur in self.currently_in_stack:
            return True

        if cur in self.visited:
            return False

        self.visited.add(cur)
        self.currently_in_stack.add(cur)

        for n in self.graph[cur]:
            if (cur,n) in self.edges_used:
                continue
            self.edges_used.add((cur,n))
            self.edges_used.add((n, cur))
            if self.inner(n):
                return True

        self.currently_in_stack.remove(cur)
        return False

    def has_cycle(self):
        self.visited = set()
        self.currently_in_stack = set()
        self.edges_used = set()
        for v in self.graph.keys():
            if self.inner(v):
                return True

        return False

    def create_graph(self, edges):
        graph = {}
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].add(edge[1])
            else:
                graph[edge[0]] = {edge[1]}
            if edge[1] in graph:
                graph[edge[1]].add(edge[0])
            else:
                graph[edge[1]] = {edge[0]}

        return graph

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]: #684 Verified on Leetcode
        self.graph = self.create_graph(edges)

        for i in range(len(edges) - 1, -1, -1):
            edge = edges[i]
            self.graph[edge[0]].remove(edge[1])
            self.graph[edge[1]].remove(edge[0])
            if not self.has_cycle():
                return edge

            self.graph[edge[0]].add(edge[1])
            self.graph[edge[1]].add(edge[0])

        assert False


if __name__ == '__main__':
    print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 1]]))
    # print(Solu)
