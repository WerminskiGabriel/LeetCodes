class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
       
        result = 0
        emptyBottles = 0

        while numBottles > 0 :
            result += numBottles
            
            emptyBottles += numBottles
            
            numBottles = emptyBottles // numExchange
            emptyBottles -= numBottles * numExchange
            
        return result 
    