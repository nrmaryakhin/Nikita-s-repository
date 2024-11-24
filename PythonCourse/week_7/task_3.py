"""https://leetcode.com/problems/find-all-anagrams-in-a-string/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        pdict = Counter(p)
        indices = []
        i, j = 0, 0
        while j < n:
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                if pdict == Counter(s[i : j + 1]):
                    indices.append(i)
                i += 1
                j += 1
        return indices
