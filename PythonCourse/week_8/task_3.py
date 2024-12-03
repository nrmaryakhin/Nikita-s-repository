"""https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {0: 1}
        pSum = 0
        ans = 0
        for i, num in enumerate(nums):
            pSum += num
            need = pSum - goal
            if need in d:
                ans += d[need]
            d[pSum] = d.get(pSum, 0) + 1
        return ans
