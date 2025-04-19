from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]): # Verified on Leetcode #900
        self.arr = []
        self.cur = 0
        self.pos = 0
        for i in range(0, len(encoding), 2):
            self.arr.append((encoding[i], encoding[i + 1]))

    def next(self, n: int) -> int:
        if self.pos == len(self.arr):
            return -1
        if self.cur == self.arr[self.pos][0]:
            self.pos += 1
            self.cur = 0
        while n > 0 and self.pos < len(self.arr):
            if n <= self.arr[self.pos][0] - self.cur:
                self.cur += n
                break
            else:
                n -= (self.arr[self.pos][0] - self.cur)
                self.cur = 0
                self.pos += 1

        return self.arr[self.pos][1] if self.pos < len(self.arr) else -1


if __name__ == '__main__':
    rle = RLEIterator([811,903,310,730,899,684,472,100,434,611])
    vals = [[358],[345],[154],[265],[73],[220],[138],[4],[170],[88]]

    result = []
    for val in vals:
        result.append(rle.next(*val))
    print(result)