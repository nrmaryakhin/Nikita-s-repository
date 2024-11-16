"""https://leetcode.com/problems/longest-turbulent-subarray/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        sign = 1 if arr[0] > arr[1] else -1

        ans = 1
        streak = 1

        for i in range(1, len(arr)):
            diff = arr[i - 1] - arr[i]
            diff *= sign

            if diff > 0:
                streak += 1
                sign *= -1
                ans = max(ans, streak)
            elif diff < 0:
                streak = 2
            else:
                streak = 1
                if i + 1 < len(arr):
                    sign = 1 if arr[i] > arr[i + 1] else -1

        return ans
