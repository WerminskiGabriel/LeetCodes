class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        result = [0] * n

        for i in range( n//2 ) :
            result[i] = i+1
            result[-(i+1)] = -(i+1)
        
        return result 
            
