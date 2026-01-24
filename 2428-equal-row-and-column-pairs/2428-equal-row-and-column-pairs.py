class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict( int )
        for row in grid :
            rows[ tuple( row ) ] += 1
        cnt = 0
        length = len( grid )
        for i in range( length ):
            col = tuple( [ grid[j][i] for j in range( length ) ] )
            cnt += rows[col] if col in rows else 0
        return cnt