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
        result = [root.val]
        lvl_floor = 0

        def rec( lvl , head ) :
            nonlocal lvl_floor
            lvl += 1

            if head.right is not None :
                if lvl  > lvl_floor :
                    lvl_floor = lvl
                    result.append( head.right.val )
                rec( lvl , head.right )

            if head.left is not None :
                if lvl > lvl_floor :
                    lvl_floor = lvl
                    result.append( head.left.val )
                rec( lvl, head.left )

            return
        rec( 0 , root )
        return result