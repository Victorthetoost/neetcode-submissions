# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if both left 
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        #both right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        # one left one right
        if p.val > root.val and q.val < root.val:
            return root
        # one right one left
        if p.val < root.val and q.val > root.val:
            return root
        # root is p or q
        if p.val == root.val or q.val == root.val:
            return root

        