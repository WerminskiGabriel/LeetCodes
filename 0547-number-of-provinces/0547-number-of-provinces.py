class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:   
            
        n = len( isConnected )
        visited = [False] * n
        adj_list = [ [ ] for i in range( n ) ]

        for i in range( n ) :
            for j in range( n ) :
                if j != i and isConnected[i][j] == 1 :
                    adj_list[i].append(j)


        def dfs( i ) :
            visited[i] = True
            for j in adj_list[i] :
                if not visited[j] :
                    dfs( j )

        cnt = 0
        for i in range( n ) :
            if not visited[i] :
                dfs( i )
                cnt += 1
        return cnt