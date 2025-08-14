class Solution:
    def integerReplacement(self, n: int) -> int:
        def rec( x ) :
            if x == 1 :
                return 0

            if x%2 == 0 :
                res = rec( x//2 ) + 1
            else :
                res = min( rec( x+1 )+1 , rec( x-1)+ 1 )

            return res
        return rec( n )