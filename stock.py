from functools import lru_cache

class Solution(object): # LeetCode #188 Add Caching to reduce Time Needed.

    def inner(self, attemptsLeft, boughtAtPrice, cur_day):
        if cur_day == len(self.prices):
            return 0

        if boughtAtPrice is not None:
            # if bought already, then sell OR not sell
            temp1 = self.prices[cur_day] - boughtAtPrice + self.inner(attemptsLeft, None, cur_day + 1)

            temp2 = float('-inf')
            if cur_day != len(self.prices) - 1:
                temp2 = self.inner(attemptsLeft, boughtAtPrice, cur_day + 1)
            return max(temp1, temp2)

        if attemptsLeft == 0 or cur_day == len(self.prices) - 1:
            return 0

        # If not bought, then buy OR not buy
        return max([
            self.inner(attemptsLeft - 1, self.prices[cur_day], cur_day + 1),
            self.inner(attemptsLeft, None, cur_day + 1)
        ])

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        self.prices = prices
        res = self.inner(k, None, 0)
        return res


if __name__ == "__main__":
    print(Solution().maxProfit(2, [3, 2, 6, 5, 0,3]))