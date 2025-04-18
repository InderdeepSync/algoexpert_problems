class Solution:

    def inner(self, s_p, p_p):
        p = self.p
        s = self.s

        while s_p >= 0 and p_p >= 0:
            if s[s_p] == p[p_p] or p[p_p] == '.':
                s_p -= 1
                p_p -= 1
            elif p[p_p] == "*":
                prev_ch = p[p_p - 1]
                p_p -= 2

                while s_p >= 0:
                    if self.inner(s_p, p_p):
                        return True
                    if prev_ch != '.' and s[s_p] != prev_ch:
                        return False
                    s_p -= 1

            else:
                return False

        while p_p >= 1 and p[p_p] == '*':
            p_p -= 2


        return s_p == -1 and p_p == -1

    def isMatch(self, s: str, p: str) -> bool: # Verified on Leetcode #10
        self.s = s
        self.p = p
        return self.inner(len(s) - 1, len(p) - 1)


if __name__ == '__main__':
    print(Solution().isMatch("aa", "c*a*"))
