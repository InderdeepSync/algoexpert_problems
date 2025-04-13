import math


class Solution(object):
    def minEatingSpeed(self, piles, h): # Accepted on Leetcode
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        start = 1
        end = max(piles)

        res = sum(piles)
        while start <= end:
            mid = (start + end) // 2

            hours = sum(map(lambda x:math.ceil(x / mid), piles))

            if hours > h:
                start = mid + 1
            elif hours <= h:
                res = min(mid, res)
                end = mid - 1
        return res
if __name__ == "__main__":
    print(Solution().minEatingSpeed([3,6, 7, 11], 8))