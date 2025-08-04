class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = lambda x : x == "1"
        res = []
        for i in range( n+1 ) :
            res.append( sum( map( cnt , bin( i )[2:] ) ))
        return res