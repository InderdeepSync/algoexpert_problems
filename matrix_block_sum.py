from typing import List


class Solution:

    def create_arr(self, mat):
        arr = [mat[i][:] for i in range(len(mat))]

        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i-1][j-1]

        return arr

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        [[1,2,3],
         [4,5,6],
         [7,8,9]]
        """
        for row in mat:
            row.insert(0, 0)
        mat.insert(0, [0] * (len(mat[0])))
        sums = self.create_arr(mat)
        print(sums)
        res = [[0] * (len(mat[0]) - 1) for _ in range(1, len(mat))]
        print(res)

        for i in range(len(res)):
            for j in range(len(res[0])):
                t_l = max(i - k, 0), max(j - k, 0)
                b_r = min(i + k, len(res) - 1), min(j + k, len(res[0]) - 1)
                res[i][j] = sums[1 + b_r[0]][1 + b_r[1]] - sums[1 + t_l[0] - 1][1 + b_r[1]] - sums[1 + b_r[0]][1 + t_l[1] - 1] + sums[1 + t_l[0] - 1][1 + t_l[1] - 1]
        return res


if __name__ == "__main__":
    print(Solution().matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))