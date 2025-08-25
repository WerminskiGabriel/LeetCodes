class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
            
        res = []

        m = len( mat )
        n = len( mat[0] )

        i , j = 0 , 0

        while i < m and j < n :
            
            #up-right
            while i >= 0 and j < n :
                res.append( mat[i][j] )
                i -= 1
                j += 1
            #re-placing
            i += 1
            if j == n :
                i += 1
                j -= 1
            
            #down-left
            while i < m and j >= 0 :
                res.append( mat[i][j] )
                i += 1
                j -= 1
            #re-placing
            j += 1
            if i == m :
                i -= 1
                j += 1

        return res