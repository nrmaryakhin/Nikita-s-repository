"""https://leetcode.com/problems/longest-repeating-character-replacement/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        maxSub = 0
        counts = {}

        while end < len(s):

            windowStart = s[start]
            windowEnd = s[end]

            counts[windowEnd] = counts.get(windowEnd, 0) + 1
            maxCount = max(counts.values())

            if end - start + 1 - maxCount > k:
                counts[windowStart] -= 1
                start += 1

            maxSub = max(maxSub, end - start + 1)
            end += 1

        return maxSub
