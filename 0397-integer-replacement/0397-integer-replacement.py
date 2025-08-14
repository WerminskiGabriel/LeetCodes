class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}
        def rec( x ) :
            if x == 1 :
                return 0
            if x in memo :
                return memo[x]

            if x % 2 == 0 :
                res = rec( x // 2 ) + 1
            else :
                res = min( rec( x + 1 ) + 1, rec( x - 1 ) + 1 )

            memo[x] = res
            return res
        return rec( n )