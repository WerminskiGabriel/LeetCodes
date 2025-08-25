class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len( ratings )

        organized = sorted( [ (ratings[i] , i ) for i in range( n ) ] )

        total = 0
        dp = [1] * n
        for i in range( 1 , n ) :
            idx = organized[i][1]
            left = idx-1
            right = idx+1
            if idx-1 >= 0 and ratings[ idx-1 ] < ratings[idx] :
                dp[idx] = max( dp[idx] , dp[idx-1] + 1 )
            if idx+1 < n and ratings[ idx + 1 ] < ratings[ idx ] :
                dp[ idx ] = max( dp[ idx ], dp[ idx + 1 ] + 1 )
        print( dp )
        return sum( dp )