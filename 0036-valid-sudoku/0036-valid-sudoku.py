class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            
        n = len( board )

        cols = [ [False for i in range( n ) ] for j in range( n ) ]

        rows = [ [False for i in range( n ) ] for j in range( n ) ]

        blocks = [ [ [ False for i in range( n ) ] for j in range( 3 ) ] for k in range( 3 ) ]

        for i in range( n ) :
            for j in range( n ) :

                num = board[i][j]

                if num == "." :
                    continue

                num = int(num) - 1

                if blocks[i//3][j//3][num] or rows[i][num] or cols[j][num] :
                    return False

                blocks[i//3][j//3][num] = rows[i][num] = cols[j][num] = True

        return True