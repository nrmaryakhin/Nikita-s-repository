"""https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if node is None:
                return None
            left_right_most = dfs(node.left)
            right_right_most = dfs(node.right)
            if node.left:
                old_node_right = node.right
                node.left, node.right = None, node.left
                if left_right_most:
                    left_right_most.right = old_node_right

            if right_right_most:
                return right_right_most
            elif left_right_most:
                return left_right_most
            return node

        dfs(root)
