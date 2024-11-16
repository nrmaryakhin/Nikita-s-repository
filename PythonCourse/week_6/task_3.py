"""https://leetcode.com/problems/find-k-closest-elements/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right, mid = 0, len(arr) - k, 0
        while left < right:
            mid = left + ((right - left) >> 1)
            if abs(arr[mid + k] - x) >= abs(arr[mid] - x) and arr[mid + k] >= x:
                right = mid
            else:
                left = mid + 1

        return arr[left : left + k]
