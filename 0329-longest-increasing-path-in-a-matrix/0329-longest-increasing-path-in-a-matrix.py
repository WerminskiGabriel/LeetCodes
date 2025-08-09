class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
            
        memo = { }

        n , m = len ( matrix ) , len( matrix[0] )

        def check_matrix( i , j , x ,y ) :
            return matrix[i][j] < matrix[x][y]

        def rec( i, j ) :
            if (i, j ) in memo :
                return memo[(i, j )]

            nonlocal m , n
            flag = False
            res = 1

            new_i , new_j = i , j+1 # right
            if new_j < m and check_matrix(i,j,new_i,new_j) :
                res = rec( new_i , new_j ) + 1
                flag = True

            new_j = j - 1 # left
            if new_j >= 0 and check_matrix(i,j,new_i,new_j) :
                res = max( res , rec( new_i, new_j ) + 1 )
                flag = True

            new_i , new_j = i-1 , j # top
            if new_i >= 0 and check_matrix(i,j,new_i,new_j) :
                res =max( res ,  rec( new_i, new_j ) + 1 )
                flag = True

            new_i = i+1 # bottom
            if new_i < n and check_matrix(i,j,new_i,new_j) :
                res = max( res , rec( new_i, new_j ) + 1 )
                flag = True

            if not flag :
                memo[ (i,j) ] = 1
                return 1

            memo[ (i,j) ] = res
            return res

        res = 1
        for i in range( n ) :
            for j in range( m ) :
                res = max( rec( i , j ) , res )

        return res