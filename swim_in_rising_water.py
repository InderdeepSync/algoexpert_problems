class Solution(object):

    def get_neighbors(self, cur):
        x, y = cur

        directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        result = []
        for d in directions:
            if not 0 <= d[0] < len(self.grid):
                continue
            if not 0 <= d[1] < len(self.grid[0]):
                continue
            if d in self.visited:
                continue
            if self.time >= self.grid[d[0]][d[1]] and self.time >= self.grid[x][y]:
                result.append(d)

        return result

    def inner(self, cur):
        if cur == self.target:
            return True

        if cur in self.visited:
            return False

        self.visited.add(cur)

        for n in self.get_neighbors(cur):
            if self.inner(n):
                return True
        return False

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.time = 0
        self.target = (len(grid) - 1, len(grid[0]) - 1)

        while True:
            self.visited = set()
            if self.inner((0, 0)):
                return self.time

            self.time += 1


if __name__ == "__main__":
    print(Solution().swimInWater([[0,2],
                                [1,3]]))