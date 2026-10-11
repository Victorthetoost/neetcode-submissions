# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(root, sub):
            # check that they look the same
            same = False
            if root.left is None and sub.left is not None:
                return False
            if root.right is None and sub.right is not None:
                return False
            if sub.left is None and root.left is not None:
                return False
            if sub.right is None and root.right is not None:
                return False
            if sub.val == root.val:
                same = True
            if sub.right:
                same = same and check(root.right, sub.right)
            if sub.left:
                same = same and check(root.left, sub.left)
            
            return same


        def find(root):
            found = False
            if root.val == subRoot.val:
                found = check(root,subRoot)
            if root.right is not None and not found:
                found =  find(root.right)
            if root.left is not None and not found:
                found = find(root.left)

            return found

        return find(root)
