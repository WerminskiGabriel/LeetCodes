class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
            
        def dfs( u ) :
            nonlocal cnt
            visited[u] = True
            for v in adj_list[u] :
                vr = abs( v )
                if not visited[vr] :
                    if v > 0 :
                        cnt += 1
                    dfs( vr)

        visited = [False] * n
        cnt = 0

        adj_list = [ [] for i in range( n ) ]
        for i , j in connections :
            adj_list[i].append( j )
            adj_list[j].append( -i )

        for u in range( n ) :
            if not visited[u] :
                dfs( u )

        return cnt