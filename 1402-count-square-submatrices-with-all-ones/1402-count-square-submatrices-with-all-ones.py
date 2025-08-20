class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
            
        m = len( matrix )
        n = len( matrix[0] )

        res = sum( matrix[0] )
        for i in range( 1 , m ) :
            res += matrix[i][0]

        def check_square( i , j ,  m ) :
            return matrix[i][j]>=m and matrix[i-1][j-1]>=m and matrix[i-1][j]>=m and matrix[i][j-1]>=m

        for i in range( 1 , m ) :
            for j in range( 1 , n ) :
                for k in range( 1 , n ) :
                    if i >= k and j >= k and check_square( i , j , k ) :
                        matrix[i][j] += 1
                    else :
                        break

                res += matrix[i][j]

        return res