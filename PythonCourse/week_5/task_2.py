"""https://leetcode.com/problems/valid-sudoku/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                box_index = (i // 3) * 3 + (j // 3)
                if num in rows[i] or num in columns[j] or num in boxes[box_index]:
                    return False
                rows[i].add(num)
                columns[j].add(num)
                boxes[box_index].add(num)
        return True
