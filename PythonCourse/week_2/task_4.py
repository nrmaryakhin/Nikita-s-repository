"""https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def f(s_c, wordDict, d={}):
            if s_c in d:
                return d[s_c]
            if not s_c:
                return True
            for word in wordDict:
                if s_c.startswith(word):
                    new_s = s_c[len(word) :]
                    if f(new_s, wordDict, d):
                        d[s_c] = True
                        return True
            d[s_c] = False
            return False

        return f(s, wordDict)
