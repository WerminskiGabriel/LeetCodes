class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict

        matrix = defaultdict( dict )
        for l , val in zip( equations , values ) :
            a , b = l[0] , l[1]
            matrix[ a ][ b ] =  val
            matrix[ b ][ a ] =  1 / val
            matrix[a][a] = matrix[b][b] = 1.0

        

        for k in matrix :
            for i in matrix[k] :
                for j in matrix[k] :
                    matrix[i][j] = matrix[i][k] * matrix[k][j] if i != j else 1.0
        res = []
        for l in queries :
            a , b = l[0] , l[1]
            
            res.append( matrix[a].get( b , -1 ) )
        return res