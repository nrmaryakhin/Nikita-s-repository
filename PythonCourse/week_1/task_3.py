"""https://leetcode.com/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=string"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        m = 0
        for i in range(len(s)):
            p1, p2 = i, i
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                if (p2 - p1 + 1) > m:
                    m = p2 - p1 + 1
                    ans = s[p1 : p2 + 1]
                p1 -= 1
                p2 += 1

            p1, p2 = i, i + 1
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                if p2 - p1 + 1 > m:
                    m = p2 - p1 + 1
                    ans = s[p1 : p2 + 1]
                p1 -= 1
                p2 += 1
        return ans
