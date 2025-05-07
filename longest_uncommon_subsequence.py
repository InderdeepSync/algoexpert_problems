from typing import List


class Solution:

    def is_subsequence(self, s1, s2, idx1=0, idx2=0):
        if idx1 == len(s1):
            return True

        if idx2 == len(s2):
            return False

        if s1[idx1] == s2[idx2]:
            return self.is_subsequence(s1, s2, idx1 + 1, idx2 + 1)

        return self.is_subsequence(s1, s2, idx1, idx2 + 1)


    def is_subsequence_outer(self, s1, seen):
        for s2 in seen:
            if self.is_subsequence(s1, s2):
                return True
        return False

    def findLUSlength(self, strs: List[str]) -> int: #522 Longest Uncommon Subsequence
        strs.sort(key=len, reverse=True)

        prev = set()
        prev_length = float('-inf')
        seen = set()

        for i in range(len(strs)):
            cur = strs[i]

            if len(cur) == prev_length:
                prev.discard(cur)
            elif len(prev) > 0:
                break

            if not self.is_subsequence_outer(cur, seen):
                prev.add(cur)

            prev_length = len(cur)
            seen.add(cur)

        return len(prev.pop()) if prev else -1


if __name__ == '__main__':
    print(Solution().findLUSlength(["aabbcc", "aabbcc","cb"]))
    print(Solution().is_subsequence("cb", "bb"))



