class Solution:
    def numTilings(self, n: int) -> int:
        
        dp = [ 0 ] * ( max( 2 , n ) )
        dp[ 0 ] = 1
        dp[ 1 ] = 2
        q = 1e9 + 7
        for i in range( 2, n ) :
            dp[ i ] = dp[ i - 1 ] * 2 + 1
            if i - 3 >= 0 :
                dp[ i ] += dp[ i - 3 ] - 1
            dp[i] %= q
        return int( dp[n-1] )