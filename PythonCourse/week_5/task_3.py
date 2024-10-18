"""https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in num_set:
                length = 1

                while n + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest
