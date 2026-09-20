# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not subRoot:
            return True

        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))



    def isSameTree(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.isSameTree(left.left, right.left) and self.isSameTree(left.right, right.right)

        else:
            return False