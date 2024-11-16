"""https://leetcode.com/problems/arithmetic-slices/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            temp = nums[i : 3 + i]
            a = temp[1] - temp[0]
            b = temp[2] - temp[1]
            if a == b:
                count = count + 1
                for j in range(i + 3, len(nums)):
                    temp.append(nums[j])
                    if a == (temp[-1] - temp[-2]):
                        count = count + 1
                    else:
                        break
        return count
