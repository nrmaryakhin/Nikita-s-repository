"""https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p_l = 0
        p_r = len(height) - 1
        max_con = 0
        while p_l < p_r:
            curr_con = min(height[p_l], height[p_r]) * (p_r - p_l)
            max_con = max(max_con, curr_con)
            if height[p_l] < height[p_r]:
                p_l += 1
            else:
                p_r -= 1
        return max_con
