class Solution:
    def canTransform(self, start: str, result: str) -> bool: #777 Verified on Leetcode
        '''
        L -> X (cannot be done, or would have been done earlier)
        X -> L (peak ahead)

        R -> X (peak ahead)
        X -> R (no!)

        XXL
        LXX

        RXX
        XXR
        '''

        s_idx = 0
        r_idx = 0

        start = list(start)
        result = list(result)

        while s_idx < len(start) and r_idx < len(result):
            if start[s_idx] == result[r_idx]:
                s_idx += 1
                r_idx += 1
                continue

            if start[s_idx] == 'L' and result[r_idx] in ('X', 'R'):
                return False
            if start[s_idx] == 'X' and result[r_idx] == 'R':
                return False
            if start[s_idx] == 'R' and result[r_idx] == 'L':
                return False

            if start[s_idx] == 'X' and result[r_idx] == 'L':
                ch_needed = 'L'
                temp = s_idx + 1
                while True:
                    if temp == len(start) or start[temp] == 'R':
                        return False
                    if start[temp] == ch_needed:
                        break
                    temp += 1

                start[temp], start[s_idx] = start[s_idx], start[temp]

            elif start[s_idx] == 'R' and result[r_idx] == 'X':
                ch_needed = 'X'
                temp = s_idx + 1
                while True:
                    if temp == len(start) or start[temp] == 'L':
                        return False
                    if start[temp] == ch_needed:
                        break
                    temp += 1

                start[temp], start[s_idx] = start[s_idx], start[temp]

            s_idx += 1
            r_idx += 1

        return s_idx == len(start) and r_idx == len(result)

if __name__ == '__main__':
    s = Solution()
    print(s.canTransform("X", "L"))