"""https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans, queue = 0, deque()
        queue.append(s)

        while queue:
            word = queue.pop()
            if len(word) > ans:
                c = Counter(word)
                if min(c.values()) >= k:
                    ans = len(word)
                else:
                    for ch in c:
                        if c[ch] < k:
                            word = word.replace(ch, "X")
                    queue.extend(word.strip("X").split("X"))

        return ans
