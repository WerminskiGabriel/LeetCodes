class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len( nums )
        m = 0
        i = 0
        while i < n and m >= i :
            if i + nums[i] > 0 :
                m = max( m, i + nums[ i ] )
            i += 1
        return m >= n-1
