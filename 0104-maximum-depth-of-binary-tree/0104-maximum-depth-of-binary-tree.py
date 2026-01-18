# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        
        def dive( head , depth ) :
            
            left_dive = dive( head.left , depth + 1 ) if head.left is not None else 0
            right_dive = dive( head.right , depth + 1 ) if head.right is not None else 0

            return max( depth , left_dive , right_dive )

        return dive( root , 1 )