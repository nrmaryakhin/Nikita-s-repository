"""https://leetcode.com/problems/rotate-image/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row = len(matrix)
        for i in range(0, row):
            for j in range(0, i + 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(0, row):
            matrix[i] = matrix[i][::-1]

        return matrix[::-1]
