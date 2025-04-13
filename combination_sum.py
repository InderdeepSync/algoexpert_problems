class Solution(object):

    def inner(self, s, goal):
        result = []

        if self.nums[s] == goal:
            result.append([self.nums[s]])

        if s == len(self.nums) - 1:
            return result

        for c in self.inner(s + 1, goal):
            result.append(c)

        if self.nums[s] < goal:
            for c in self.inner(s + 1, goal - self.nums[s]):
                c.insert(0, self.nums[s])
                result.append(c)

        return result

    def combinationSum2(self, candidates, target): # butATM
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        self.nums = candidates
        self.nums.sort()

        result = []
        seen = set()
        for c in self.inner(0, target):
            if tuple(c) in seen:
                continue
            seen.add(tuple(c))
            result.insert(0, c)
        return result



if __name__ == '__main__':
    print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))