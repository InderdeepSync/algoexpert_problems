
from typing import List
from functools import lru_cache

# TODO: Look at optimal solution Also.
class Solution: # Leetcode #435 TimeLimitExceeded
    # https: // leetcode.com / problems / non - overlapping - intervals / solutions / 6066007 / 45 - ms - runtime - beats - 95 - user - confirm - step - by - steps - solution - beginner - friendly /?envType = problem - list - v2 & envId = oizxjoit
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        @lru_cache()
        def inner(start):
            if len(intervals) - start <= 1:
                return 0

            i = start + 1
            while i < len(intervals) and intervals[start][1] > intervals[i][0]:
                i += 1

            return min((i - 1 - start) + inner(i), 1 + inner(start + 1))

        intervals.sort()
        return inner(0)


if __name__ == "__main__":
    print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))

