class Solution:
    def jump(self, nums: List[int]) -> int:
        inf = float( "inf" )
        n = len( nums )
        dp = [inf] * n
        dp[0] = 0

        for i in range( n ) :
            for j in range( min( i + nums[i] , n-1 ) , i , -1 ) :
                if j == n-1 :
                    return dp[i] + 1 
                dp[j] = min( dp[j] , dp[i] + 1 )
        return dp[n-1]