

class Solution: # Verified on Leetcode #647
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += 1
            temp = 1
            while i - temp >= 0 and i + temp < len(s) and s[i - temp] == s[i + temp]:
                count += 1
                temp += 1

        for i in range(len(s) - 1):
            j = i + 1
            temp = 0
            while i - temp >= 0 and j + temp < len(s) and s[i - temp] == s[j + temp]:
                count += 1
                temp += 1

        return count



if __name__ == "__main__":
    result = Solution().countSubstrings("abc")
    print(result)