"""https://leetcode.com/problems/fruit-into-baskets/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 2:
            return len(fruits)
        arr = []
        ct = 1
        p = 0
        for i in range(1, len(fruits)):
            if fruits[i] != fruits[p]:
                arr.append([fruits[p], ct])
                ct = 1
                p = i
            else:
                ct += 1
        arr.append([fruits[-1], ct])
        print(arr)
        if len(arr) == 1:
            return arr[0][1]
        ct = arr[0][1] + arr[1][1]
        mx = ct
        art = [arr[0][0], arr[1][0]]

        for i in range(2, len(arr)):
            if arr[i][0] not in art:
                # print(art,ct)
                mx = max(ct, mx)
                ct = arr[i][1] + arr[i - 1][1]
                art = [arr[i][0], arr[i - 1][0]]
            else:
                ct += arr[i][1]
        mx = max(mx, ct)
        return mx
