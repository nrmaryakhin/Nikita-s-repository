"""https://leetcode.com/problems/decode-ways/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == "0":
            return 0
        n = len(s)
        ans = [0] * (n + 1)
        ans[0], ans[1] = 1, 1
        for i in range(2, n + 1):
            one = int(s[i - 1])
            two = int(s[i - 2 : i])
            if one != 0:
                ans[i] += ans[i - 1]
            if 10 <= two <= 26:
                ans[i] += ans[i - 2]
        return ans[n]
