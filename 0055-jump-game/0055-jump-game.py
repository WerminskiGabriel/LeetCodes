class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len( nums ) 
        if n == 1 :
            return True

        i , m  = 0 , 0

        for i in range( n-1 ) :
            m = max( m , i + nums[i] )
            if i >= m :
                return False
            if m >= n-1 :
                return True
        
        return False
