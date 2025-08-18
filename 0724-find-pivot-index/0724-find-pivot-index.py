class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len( nums )
        left = 0
        right = sum( nums[ 1 : ] )

        for i in range( 0, n - 1 ) :
            
            if left == right :
                return i

            else :
                left += nums[ i ]
                right -= nums[ i + 1 ]
            
        return n-1 if left == right else -1