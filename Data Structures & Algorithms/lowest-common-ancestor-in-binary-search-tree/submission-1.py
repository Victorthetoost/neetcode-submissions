# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        minn = min(p.val,q.val)
        maxx = max(p.val,q.val)

        def traverse(node):
            if not node.right and not node.left:
                return node
            if node.val > minn and node.val < maxx:
                return node
            if node.val == minn or node.val == maxx:
                return node
            if node.right and node.val < minn:
                return traverse(node.right)
            if node.left and node.val > maxx:
                return traverse(node.left)
            return node

        return traverse(root)
        