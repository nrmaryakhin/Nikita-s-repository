"""https://leetcode.com/problems/majority-element-ii/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        result = []
        for num, count in counts.items():
            if count > len(nums) // 3:
                result.append(num)

        return result
