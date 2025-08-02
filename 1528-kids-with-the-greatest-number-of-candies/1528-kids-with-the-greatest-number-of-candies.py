class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        




        
        max_n = max( candies )
        leng = len( candies ) 
        
        result = [ 0 ] * leng 

        mini = max_n - extraCandies

        for i in range( leng ) : 
            if candies[i] >= mini :
                result[i] = True
            else :
                result[i] = False
        
        return result