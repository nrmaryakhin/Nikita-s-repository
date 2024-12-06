"""https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append((root, 0))
        visited = []

        while queue:
            node, level = queue.popleft()

            if node:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

                try:
                    visited[level].append(node.val)
                except:
                    visited.append([node.val])

        return visited
