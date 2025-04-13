class Solution(object):
    def wiggleSort(self, nums): # Accepted on LeetCode
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        [1, 2, 3, 4, 5] => 3, 2 ,5, 1 ,5
        """
        nums.sort()
        result = []
        if len(nums) % 2 == 0:
            i = len(nums) // 2 - 1
            while i >= 0:
                result.extend([nums[i], nums[i + len(nums) // 2]])
                i -= 1
        else:
            i = len(nums) // 2 - 1
            result.append(nums[len(nums) // 2])
            while i >= 0:
                result.extend([nums[i], nums[i + len(nums) // 2 + 1]])
                i -= 1

        nums[:] = result


if __name__ == "__main__":
    input_arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4]
    Solution().wiggleSort(input_arr)
    print(input_arr)