class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def rec( x ) :


            if x < 0  :
                return 0
            if x <= 1 :
                return 1

            if x in memo :
                return memo[x]

            nonlocal n
            res = 1
            for i in range( 2 , x+1 if n != x else x ) :
                res = max( res, rec( x - i ) * i )
            memo[x] = res
            return res

        return rec( n )