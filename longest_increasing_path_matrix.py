class Solution(object):

    def get_neighbors(self, cur, visiting):
        x, y = cur
        directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        result = []
        for d in directions:
            if not 0 <= d[0] <= len(self.matrix) - 1:
                continue
            if not 0 <= d[1] <= len(self.matrix[0]) - 1:
                continue
            if self.matrix[d[0]][d[1]] > self.matrix[x][y] and d not in visiting:
                result.append(d)
        return result

    def traverse(self, cur, visiting, temp):
        if cur in temp:
            return temp[cur]
        visiting.add(cur)

        neighbors = self.get_neighbors(cur, visiting)

        depths = []
        for n in neighbors:
            t1 = self.traverse(n, visiting, temp)
            depths.append(t1)

        temp[cur] = 1 + (max(depths) if depths else 0)
        visiting.remove(cur)
        return temp[cur]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.matrix = matrix
        temp = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) not in temp:
                    self.traverse((i, j), visiting=set(), temp=temp)

        return max(temp.values())



if __name__ == '__main__':
    print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))