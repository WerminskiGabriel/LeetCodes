class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def rec( i ) :
            if i in memo : 
                return memo[i]
            
            if i <= 1  :
                memo[i] = 1
                return 1
            
            res = rec( i-1 ) + rec( i-2 )
            memo[i] = res
            return res
            
        return rec( n )