class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len( grid )
        n = len( grid[0] )

        for i in range( m ) :
            if i == 0 :
                j = 0
                p = i
                q = j
                tempArr = [ ]
                while p < m and q < n :
                    tempArr.append( grid[ p ][ q ] )
                    p += 1
                    q += 1
                tempArr.sort( reverse = True )
                p = i
                q = j
                k = 0
                while p < m and q < n :
                    grid[ p ][ q ] = tempArr[ k ]
                    p += 1
                    q += 1
                    k += 1

                for j in range( 1 , n ) :
                    p = i
                    q = j
                    tempArr = []
                    while p < m and q < n :
                        tempArr.append( grid[p][q] )
                        p += 1
                        q += 1
                    tempArr.sort()
                    p = i
                    q = j
                    k = 0
                    while p < m and q < n :
                        grid[p][q] = tempArr[k]
                        p += 1
                        q += 1
                        k += 1

            else :
                j = 0
                p = i
                q = j
                tempArr = [ ]
                while p < m and q < n :
                    tempArr.append( grid[ p ][ q ] )
                    p += 1
                    q += 1
                tempArr.sort(reverse=True)
                p = i
                q = j
                k = 0
                while p < m and q < n :
                    grid[ p ][ q ] = tempArr[ k ]
                    p += 1
                    q += 1
                    k += 1
        return grid