class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
            
        m = len( grid )
        n = len( grid[0] )

        dist = [ [ -1 for i in range( n ) ] for i in range( m ) ]

        from collections import deque
        q = deque()

        def bfs() :

            for i in range( m ) :
                for j in range( n ) :
                    if grid[i][j] == 2 :
                        q.append( (i,j) )
                        dist[i][j] = 0

            res = 0

            while q :

                i , j = q.popleft()

                new_i , new_j = i+1 , j
                if new_i < m and dist[new_i][new_j] == -1 and grid[new_i][new_j] != 0 :
                    dist[new_i][new_j] = dist[i][j] + 1 if grid[new_i][new_j] == 1 else 0
                    q.append( (new_i,new_j) )
                    res = max( res , dist[new_i][new_j] )

                new_i, new_j = i-1 , j
                if new_i >= 0  and dist[ new_i ][ new_j ] == -1 and grid[ new_i ][ new_j ] != 0 :
                    dist[ new_i ][ new_j ] = dist[ i ][ j ] + 1 if grid[ new_i ][ new_j ] == 1 else 0
                    q.append( (new_i,new_j) )
                    res = max( res, dist[ new_i ][ new_j ] )

                new_i, new_j = i, j+1
                if new_j < n and dist[ new_i ][ new_j ] == -1 and grid[ new_i ][ new_j ] != 0 :
                    dist[ new_i ][ new_j ] = dist[ i ][ j ] + 1 if grid[ new_i ][ new_j ] == 1 else 0
                    q.append( (new_i,new_j) )
                    res = max( res, dist[ new_i ][ new_j ] )

                new_i, new_j = i , j-1
                if new_j >= 0 and dist[ new_i ][ new_j ] == -1 and grid[ new_i ][ new_j ] != 0 :
                    dist[ new_i ][ new_j ] = dist[ i ][ j ] + 1 if grid[ new_i ][ new_j ] == 1 else 0
                    q.append( (new_i,new_j) )
                    res = max( res, dist[ new_i ][ new_j ] )

            return res

        res = bfs()

        for i in range( m ) :
            for j in range( n ) :
                if dist[i][j] == -1 and grid[i][j] == 1 :
                    return -1

        return res