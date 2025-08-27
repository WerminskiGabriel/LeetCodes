class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power_evaluate( x ) :
            if x == 1 :
                return 0

            if x in power :
                return power[x]

            if x % 2 == 0 :
                res = 1 + power_evaluate( x//2 )
            else :
                res = 1 + power_evaluate( 3*x+1 )

            power[x] = res
            return res
        power = {}
        arr = []
        for i in range( lo , hi+1 ) :
            arr.append( ( power_evaluate( i ) , i ) )
        return sorted( arr )[k-1][1]