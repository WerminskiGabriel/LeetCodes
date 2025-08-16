class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len( intervals)

        res = []

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range( 1 , n ) :
            a , b = intervals[i]
            if a <= end :
                if b > end :
                    end = b
            else :
                res.append( [start,end] )
                start , end = a , b
        res.append( [start,end])
        return res