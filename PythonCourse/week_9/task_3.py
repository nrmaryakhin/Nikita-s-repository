"""https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def more_than_one_node(node, Min, Max):
            # print(node,Min,Max)
            if not node:
                return True
            if node.val <= Min or node.val >= Max:
                return False
            return more_than_one_node(node.left, Min, node.val) and more_than_one_node(
                node.right, node.val, Max
            )

        return more_than_one_node(root, -(2**31) - 1, 2**31)
