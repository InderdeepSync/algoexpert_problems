import heapq

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        min_heap = []
        info = {}

        for num in nums:
            info[num] = info.get(num, 0) + 1

        for key in info.keys():
            heapq.heappush(min_heap, key)

        prev = None
        count = 0
        popped = set()
        while min_heap:
            val = heapq.heappop(min_heap)
            popped.add(val)

            if prev is not None and val != prev + 1:
                return False

            count += 1
            prev = val
            if count == k:
                prev = None
                count = 0
                for v in popped:
                    info[v] -= 1
                    if info[v] >= 1:
                        heapq.heappush(min_heap, v)
                popped.clear()
        return len(popped) == 0


if __name__ == '__main__':
    print(Solution().isPossibleDivide([5,7,8,8,7,4,3,6], 1))