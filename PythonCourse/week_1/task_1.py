"""https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=string&favoriteSlug=&difficulty=MEDIUM"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def f(permutation, next_vars):
            if len(next_vars) == 0:
                ans.append(permutation)
            else:
                for char in keyboard[next_vars[0]]:
                    f(permutation + char, next_vars[1::])

        ans = []
        f("", digits)
        return ans
