class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
            visited = [False] * n
            for a , b in edges :
                visited[b] = True
            
            res = []
            for i in range( n ) :
                if not visited[i] :
                    res.append( i ) 
            
            return res