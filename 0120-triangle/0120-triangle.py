class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
            
        memo = {}
        def rec( i , j ) :

            if i == len( triangle ) :
                return 0

            key = (i,j)
            if key in memo :
                return memo[key]

            current = triangle[i][j]

            res = current + min( rec( i+1 , j ) , rec( i+1 , j+1 ) )

            memo[key] = res
            return res

        return rec( 0,0 )

