
def inner(nums, prevNum):
    if not nums:
        return []
    if nums[0] <= prevNum:
        return inner(nums[1:], prevNum)

    temp1 = inner(nums[1:], prevNum)
    temp2 = [nums[0], *inner(nums[1:], nums[0])]

    return max(temp1, temp2, key=len)


def longestIncreasingSubsequence(array): # Verified on AlgoExpert
    return inner(array, float("-inf"))


if __name__ == "__main__":
    print(longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))
