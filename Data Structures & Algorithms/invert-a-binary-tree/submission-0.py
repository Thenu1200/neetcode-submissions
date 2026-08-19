'''
make a dummy = root
make a tempnode = dummy.left
dummy.left = dummy.right
dummy.right = tempnode

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (not root): return root
        returnnode = root
        dummy = root
        tempnode = dummy.left
        dummy.left = dummy.right
        dummy.right = tempnode
        if (dummy.left):
            dummy.left = self.invertTree(dummy.left)
        if (dummy.right):
            dummy.right = self.invertTree(dummy.right)
        return returnnode
