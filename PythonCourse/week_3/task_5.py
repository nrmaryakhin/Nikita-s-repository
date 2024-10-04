"""https://leetcode.com/problems/maximum-gap/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        diff = -100000000000
        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i - 1]
            diff = max(curr_diff, diff)
        return diff
