# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None :
            return []
        result = []

        def rec( lvl , head ) :
            if len( result ) == lvl :
                result.append( head.val)
            if head.right is not None :
                rec( lvl+1 , head.right )
            if head.left is not None :
                rec( lvl+1, head.left )

        rec( 0 , root )
        return result