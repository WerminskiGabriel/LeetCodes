class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
        def rec( i , j , dir_idx , madeTurn , required ) :
            
            if i < 0 or j < 0 or i >= m or j >= n or required != grid[i][j] :
                return 0
            
            key = ( i , j , dir_idx , madeTurn , required )
            if key in memo :
                return memo[key]

            if required == 0 or required == 1 :
                new_required = 2
            else :
                new_required = 0

            res = 1 + rec( i + dirs[dir_idx][0] , j + dirs[dir_idx][1] , dir_idx , madeTurn , new_required )
            if not madeTurn :
                dir_idx = 0 if dir_idx == 3 else dir_idx + 1
                res = max( res , 1 + rec( i + dirs[dir_idx][0] , j + dirs[dir_idx][1] , dir_idx , True , new_required) )
            
            memo[key] = res
            return res


        m = len( grid )
        n = len( grid[0] )

        #        tr       tl        br       bl
        dirs = [ (-1,1) , (1,1), (1,-1) , (-1,-1) ]
        res = 0
        memo = {}

        for i in range( m ) :
            for j in range( n ) :
                if grid[i][j] == 1 :
                    for k in range( 4 ) :
                        res = max( res , rec( i , j , k , False , 1 ) )
        return res