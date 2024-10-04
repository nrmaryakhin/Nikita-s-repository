"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sums = numbers[l] + numbers[r]
            if sums < target:
                l += 1
            elif sums > target:
                r -= 1
            else:
                return [l + 1, r + 1]
