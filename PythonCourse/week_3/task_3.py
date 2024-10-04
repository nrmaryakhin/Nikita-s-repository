"""https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        if len(ans) == 0:
            return [-1, -1]
        elif len(ans) == 1:
            return ans * 2
        else:
            return [ans[0], ans[-1]]
