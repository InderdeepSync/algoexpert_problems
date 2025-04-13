class Solution(object):

    def getProduct(self, start, end):
        result = self.nums[start]
        for i in range(start + 1, end + 1):
            result = result * self.nums[i]

        return result

    def inner(self, start, end):
        if start == end:
            return self.nums[start]
        negativeCount = 0
        first = None
        last = None
        for i in range(start, end + 1):
            if self.nums[i] < 0:
                negativeCount += 1
                if first is None:
                    first = i
                last = i

        if negativeCount % 2 == 0:
            return self.getProduct(start, end)
        else:
            possibilities = []
            if end - first >= 1:
                possibilities.append(self.getProduct(first + 1, end))

            if last - start >= 1:
                possibilities.append(self.getProduct(start, last - 1))
            return max(possibilities)

    def maxProduct(self, nums): # Accepted LeetCode #152
        """
        :type nums: List[int]
        :rtype: int
        """

        self.nums = nums

        res = float('-inf')
        prevZero = -1
        for i, val in enumerate(nums):
            if val == 0:
                res = max(res, self.inner(prevZero + 1, i - 1))
                prevZero = i

        if prevZero != -1:
            res = max(res, 0)

        if prevZero != len(nums) - 1:
            res = max(res, self.inner(prevZero + 1, len(nums) - 1))

        return res


if __name__ == '__main__':
    print(Solution().maxProduct([-3, 0, 1,-2]))