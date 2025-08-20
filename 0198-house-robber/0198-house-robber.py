class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len( nums )
        dp = [ 0 for i in range( n+1 ) ]
        dp[1] = nums[0]

        for j in range( 2,n+1 ) :
            dp[j] = max( dp[j-2] + nums[j-1] , dp[j-1] )
        return dp[n]