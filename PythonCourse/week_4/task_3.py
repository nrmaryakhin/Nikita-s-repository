"""https://leetcode.com/problems/maximum-subarray/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -10000
        for n in nums:
            curr_sum += n
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
