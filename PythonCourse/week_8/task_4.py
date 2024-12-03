"""https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        i = 0
        j = 0
        n = len(nums)
        z = 0

        while j < n:
            if nums[j] == 1:
                ans = max(ans, j - i + 1)
            else:
                z += 1
                if z <= k:
                    ans = max(ans, j - i + 1)
                else:
                    while i <= j and z > k:
                        if nums[i] == 0:
                            z -= 1
                        i += 1
            j += 1

        return ans
