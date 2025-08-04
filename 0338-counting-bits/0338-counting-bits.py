class Solution:
    def countBits(self, n: int) -> List[int]:
        n += 1
        dp = [0] *  (n)
        q = 1
        for i in range( 1,n ) :
            if q * 2 == i :
                q = i
            dp[i] = dp[i-q] + 1
        return dp