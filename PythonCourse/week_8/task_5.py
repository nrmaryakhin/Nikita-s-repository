"""https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def getPrefix(number):
            maxSum = 0

            window = 0
            pntr = 0
            prefix = []
            while pntr < number:
                window += nums[pntr]
                if pntr == number - 1:
                    maxSum = max(maxSum, window)
                    prefix.append(window)
                else:
                    prefix.append(float("-inf"))
                pntr += 1

            while pntr < len(nums):
                window -= nums[pntr - number]
                window += nums[pntr]
                maxSum = max(maxSum, window)
                prefix.append(maxSum)
                pntr += 1

            return prefix

        def getPostfix(number):
            maxSum = 0

            window = 0
            pntr, count = len(nums) - 1, 0
            postfix = []
            while count < number:
                window += nums[pntr]
                if count == number - 1:
                    maxSum = max(maxSum, window)
                    postfix.append(window)
                else:
                    postfix.append(float("-inf"))
                count += 1
                pntr -= 1

            while pntr >= 0:
                window -= nums[pntr + number]
                window += nums[pntr]
                maxSum = max(maxSum, window)
                postfix.append(maxSum)
                pntr -= 1

            return postfix[::-1]

        prefixFirst, prefixSecond = getPrefix(firstLen), getPrefix(secondLen)
        postfixFirst, postfixSecond = getPostfix(firstLen), getPostfix(secondLen)

        print(prefixFirst, prefixSecond)

        maxSum = 0

        for i in range(len(prefixFirst) - 1):
            maxSum = max(maxSum, prefixFirst[i] + postfixSecond[i + 1])
        for i in range(len(prefixSecond) - 1):
            maxSum = max(maxSum, prefixSecond[i] + postfixFirst[i + 1])

        return maxSum
