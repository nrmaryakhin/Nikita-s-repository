"""https://leetcode.com/problems/generate-parentheses/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(l, r, s):
            if len(s) == n * 2:
                ans.append(s)
                return

            if l < n:
                f(l + 1, r, s + "(")
            if r < l:
                f(l, r + 1, s + ")")

        ans = []
        f(0, 0, "")
        return ans
