"""https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            d[sorted_word].append(word)
        return list(d.values())
