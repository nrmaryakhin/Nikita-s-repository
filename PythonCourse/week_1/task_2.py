"""https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=string&difficulty=MEDIUM"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        p1 = 0
        m = 0
        for p2 in range(len(s)):
            if s[p2] not in st:
                st.add(s[p2])
                m = max(m, p2 - p1 + 1)
            else:
                while s[p2] in st:
                    st.remove(s[p1])
                    p1 += 1
                st.add(s[p2])
        return m
