class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from collections import deque

        entrance = tuple( entrance )
        q = deque()
        q.append( entrance )

        m = len( maze )
        n = len( maze[0] )

        dist = [ [ -1 for i in range( n ) ] for i in range( m ) ]
        dist[entrance[0]][entrance[1]] = 0

        while q :
            i , j  = q.popleft()

            new_i , new_j = i+1 , j
            if new_i < m and maze[new_i][new_j] == "." and dist[new_i][new_j] == -1 :
                if new_i == m-1 or new_j == 0 or new_j == n-1 :
                    return dist[i][j] + 1
                else :
                    q.append( (new_i, new_j) )
                    dist[new_i][new_j] = dist[i][j] + 1

            new_i, new_j = i , j+1
            if new_j < n and maze[ new_i ][ new_j ] == "." and dist[ new_i ][ new_j ] == -1 :
                if new_j == n - 1 or new_i == 0 or new_i == m-1 :
                    return dist[ i ][ j ] + 1
                else :
                    q.append( (new_i, new_j) )
                    dist[ new_i ][ new_j ] = dist[ i ][ j ] + 1

            new_i, new_j = i - 1, j
            if new_i >= 0  and maze[ new_i ][ new_j ] == "." and dist[ new_i ][ new_j ] == -1 :
                if new_i == 0 or new_j == 0 or new_j == n-1 :
                    return dist[ i ][ j ] + 1
                else :
                    q.append( (new_i, new_j) )
                    dist[ new_i ][ new_j ] = dist[ i ][ j ] + 1

            new_i, new_j = i , j - 1
            if new_j >= 0 and maze[ new_i ][ new_j ] == "." and dist[ new_i ][ new_j ] == -1 :
                if new_j == 0 or new_i == 0 or new_i == m-1 :
                    return dist[ i ][ j ] + 1
                else :
                    q.append( ( new_i , new_j ) )
                    dist[ new_i ][ new_j ] = dist[ i ][ j ] + 1

        return -1