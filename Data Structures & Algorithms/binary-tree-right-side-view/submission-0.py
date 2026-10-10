# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        visited = set()
        ret = []
        def move(node, level):
            if node is None:
                return
            if level not in visited:
                visited.add(level)
                ret.append(node.val)
            if node.right != None:
                move(node.right,level + 1)
            if node.left != None:
                move(node.left,level + 1)

        move(root, 0)
        return ret
