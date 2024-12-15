"""https://leetcode.com/problems/path-sum-iii/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_paths_from_node(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0

            count = 0
            if node.val == target:
                count += 1

            count += count_paths_from_node(node.left, target - node.val)
            count += count_paths_from_node(node.right, target - node.val)

            return count

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            count = count_paths_from_node(node, targetSum)

            count += dfs(node.left)
            count += dfs(node.right)

            return count

        return dfs(root)
