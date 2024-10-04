"""https://leetcode.com/problems/jump-game/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True
