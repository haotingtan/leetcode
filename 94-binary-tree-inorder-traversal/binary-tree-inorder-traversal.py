# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        def helper(cur):
            if cur is None:
                return []

            left = helper(cur.left)
            right = helper(cur.right)

            return left + [cur.val] + right

        return helper(root)