# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
       
        while root is not None and root.val != val :
            root = root.right if root.val < val else root.left

        return None if ( root is None or root.val != val ) else root 
            
        