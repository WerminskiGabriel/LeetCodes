class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:   
        n = len( isConnected )
        visited = [False] * n

        def dfs( i ) :
            visited[i] = True
            for j in range( n ) :
                if isConnected[i][j] == 1 and not visited[j] :
                    dfs( j )

        cnt = 0
        for i in range( n ) :
            if not visited[i] :
                dfs( i )
                cnt += 1
        return cnt
            