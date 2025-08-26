class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len( graph )

        colors = [0] * n
        from collections import deque

        q = deque()
        for u in range( n ) :
            if colors[u] == 0 :  
                q.append( u )
                colors[u] = 1

                while q :
                    u = q.popleft()
                    
                    for v in graph[u] :
                        if colors[v] == 0 :
                            q.append( v )
                            colors[v] = 1 if colors[u] == 2 else 2
                        else :
                            if colors[u] == colors[v] :
                                return False

        return True