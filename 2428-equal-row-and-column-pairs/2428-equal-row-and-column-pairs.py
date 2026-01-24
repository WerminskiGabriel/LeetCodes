class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        for row in grid :
            trow = tuple( row ) 
            rows[ trow ] = rows[trow]+1 if trow in rows else 1
        cnt = 0
        length = len( grid )
        for i in range( length ):
            col = tuple( [ grid[j][i] for j in range( length ) ] )
            cnt += rows[col] if col in rows else 0
        return cnt