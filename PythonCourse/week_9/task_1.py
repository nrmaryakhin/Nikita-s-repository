"""https://leetcode.com/problems/unique-binary-search-trees-ii/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTree(left, right):
            if left > right:
                return [None]
            res = []
            for i in range(left, right + 1):
                for leftTree in generateTree(left, i - 1):
                    for rightTree in generateTree(i + 1, right):
                        root = TreeNode(i, leftTree, rightTree)
                        res.append(root)
            return res

        return generateTree(1, n)
