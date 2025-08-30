class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            
        n = len( board )

        cols = [ [False for i in range( n ) ] for j in range( n ) ]

        rows = [ [False for i in range( n ) ] for j in range( n ) ]

        blocks = [ [ [ False for i in range( n ) ] for j in range( 3 ) ] for k in range( 3 ) ]
        #return blocks

        for i in range( n ) :
            for j in range( n ) :

                num = board[i][j]

                if num == "." :
                    continue

                num = int(num) - 1
                if blocks[i//3][j//3][num] or rows[i][num] or cols[j][num] :
                    return False

                blocks[i//3][j//3][num] = True
                rows[i][num] = True
                cols[j][num] = True

        for i in range( 3 ):
            for j in range( 3 ) :
                print( i, j, blocks[ i ][ j ] )

        return True