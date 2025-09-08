class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
                
        a = n-1
        b = 1

        def check( x ):

            while x > 0 :
                if x % 10 == 0 :
                    return False
                x //= 10
            return True 
        
        while not check( a ) or not check( b ):
            m = 1
            a -= m
            b += m 
        
        return [a,b]