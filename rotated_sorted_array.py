from typing import List


class Solution: # Verified on Leetcode  #153
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while True:
            mid = (start + end) // 2

            if mid == start:
                return min(nums[end], nums[start])
            if nums[mid] < nums[end]:
                end = mid
            elif nums[start] < nums[mid]:
                start = mid


if __name__ == "__main__":
    print(Solution().findMin([11, 13, 15, 17]))



