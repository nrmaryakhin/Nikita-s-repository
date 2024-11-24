"""https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cur_pro = 1
        count = 0
        j = 0
        for i in range(len(nums)):
            cur_pro *= nums[i]
            while cur_pro >= k and j <= i:
                cur_pro //= nums[j]
                j += 1
            count += i - j + 1
        return count
