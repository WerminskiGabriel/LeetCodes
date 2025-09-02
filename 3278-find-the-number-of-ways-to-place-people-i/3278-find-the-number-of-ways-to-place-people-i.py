class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len( points )
        points.sort( key = lambda x : (-x[0] , x[1] ) )
        cnt = 0
        for i in range( n-1 ) :
            curr = float("inf")
            for j in range( i + 1 , n ) :
                if curr > points[j][1] >= points[i][1] :
                    cnt += 1
                    curr = points[j][1]
        return cnt